import mysql.connector

# Connect to MySQL database
cnx = mysql.connector.connect(user='root', password='muthu@123',
                              host='localhost', database='movie_booking_system')

# Define the cursor object
cursor = cnx.cursor()

#insert the movies
def insert_movie(movie_name, theater, timing, center, city, ticket_price):
    try:
        cursor.execute("INSERT INTO movies (movie_name, theater, timing, center, city, ticket_price) VALUES (%s, %s, %s, %s, %s, %s)", (movie_name, theater, timing, center, city, ticket_price))
        cnx.commit()
        print("New Movie Added Successfully!")
    except Exception as e:
        print("Error while inserting new movie: {}".format(e))
        cnx.rollback()


# Define the function to select a movie
def select_movie():
    cursor.execute("SELECT movie_name, theater, timing, ticket_price FROM movies")
    movies = cursor.fetchall()
    for movie in movies:
        print("Movie Name: {}\nTheater: {}\nTiming: {}\nTicket Price: {}".format(movie[0], movie[1], movie[2], movie[3]))

# Define the function to select movies based on theater, center, and city
def select_movie_by_theater(theater, center, city):
    cursor.execute("SELECT movie_name, timing, ticket_price FROM movies WHERE theater = %s AND center = %s AND city = %s",
                   (theater, center, city))
    movies = cursor.fetchall()
    for movie in movies:
        print("Movie Name: {}\nTiming: {}\nTicket Price: {}".format(movie[0], movie[1], movie[2]))

# Define the function to book movie tickets
def book_movie_tickets(customer_name, customer_email, movie_name, no_of_tickets):
    cursor.execute("SELECT ticket_price FROM movies WHERE movie_name = %s", (movie_name,))
    ticket_price = cursor.fetchone()[0]
    total_cost = ticket_price * no_of_tickets

    # Insert the customer details into the database
    cursor.execute("INSERT INTO customer (name, email) VALUES (%s, %s)", (customer_name, customer_email))
    customer_id = cursor.lastrowid

    # Insert the booking details into the database
    cursor.execute("INSERT INTO bookings (customer_id, movie_name, no_of_tickets, total_cost) VALUES (%s, %s, %s, %s)",
                   (customer_id, movie_name, no_of_tickets, total_cost))
    booking_id = cursor.lastrowid

    cnx.commit()

    print("Booking confirmed!\nBooking ID: {}\nTotal Cost: {}".format(booking_id, total_cost))

# Define the function to display the customer and theater tables
def display_tables():
    cursor.execute("SELECT * FROM customer")
    cus = cursor.fetchall()
    
    if cus:
        cust=[]
        for c in cus:
            a={
                'id':c[0],
                'name':c[1],
                'email':c[2]
            }
            cust.append(a)
        print(cust)
    cursor.execute("SELECT * FROM theater")
    theaters = cursor.fetchall()
    if theaters:
        b=[]
        for t in theaters:
            a={
                'id':t[0],
                'name':t[1],
                'address':t[2],
                'city':t[3]
            }
            b.append(a)
        print(b)
    # print("Customer Table:")
    # for customer in customers:
    #     print(customer)

    # print("\nTheater Table:")
    # for theater in theaters:
    #     print(theater)

def calculate_total_cost():
    cursor.execute("SELECT SUM(total_cost) FROM bookings")
    total_cost = cursor.fetchone()[0]
    print("Total Cost of all Bookings: {}".format(total_cost))

# Test the functions
insert_movie("LOVE TODAY", "KG", "9:00 PM", "Center 1", "madurai", 125.50)
insert_movie("PS-2", "EGA", "3:00 PM", "Center 3", "Chennai", 189.50)
select_movie()
select_movie_by_theater("Rohini", "Center 2", "City B")
select_movie_by_theater("EGA", "Center 3", "Chennai")
book_movie_tickets("Jhn Doe", "johndoe@example.com", "Movie B", 3)
calculate_total_cost()
insert_movie("Movie B", "Rohini", "7:00 PM", "Center 2", "City B", 12.50)

# Close the database connection
cursor.close()
cnx.close()