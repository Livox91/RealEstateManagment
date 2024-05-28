import mysql.connector
from mysql.connector import Error

def update_rental(connection, rental_id, listing_id, client_id, rent, duration, rental_date):
    try:
        cursor = connection.cursor()
        sql_query = """UPDATE rental SET Listing_ID = %s, Client_ID = %s, Rent = %s, Duration = %s, Rental_Date = %s WHERE Rental_ID = %s"""
        cursor.execute(sql_query, (listing_id, client_id, rent, duration, rental_date, rental_id))
        connection.commit()
        print("Rental updated successfully!")
    except Error as e:
        print(f"Error updating rental: {e}")
    finally:
        cursor.close()

try:
    connection = mysql.connector.connect(
         host="localhost",
        user="root",
        password="Manahil18!",
        database="real_estate"
    )
    if connection.is_connected():
        print("Connected to MySQL database")
except Error as e:
    print(f"Error connecting to MySQL database: {e}")

# Take user input for rental details
rental_id = int(input("Enter Rental ID to update: "))
listing_id = int(input("Enter new Listing ID: "))
client_id = int(input("Enter new Client ID: "))
rent = float(input("Enter new Rent amount: "))
duration = input("Enter new Duration: ")
rental_date = input("Enter new Rental Date (YYYY-MM-DD): ")

# Call the update_rental function with user input
update_rental(connection, rental_id, listing_id, client_id, rent, duration, rental_date)

if connection.is_connected():
    connection.close()
    print("MySQL database connection closed")
