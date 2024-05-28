import mysql.connector
from mysql.connector import Error

def update_sale(connection, sale_id, listing_id, client_id, sale_date, price):
    try:
        cursor = connection.cursor()
        sql_query = """UPDATE sale SET Listing_ID = %s, Client_ID = %s, Sale_Date = %s, Price = %s WHERE Sale_ID = %s"""
        cursor.execute(sql_query, (listing_id, client_id, sale_date, price, sale_id))
        connection.commit()
        print("Sale updated successfully!")
    except Error as e:
        print(f"Error updating sale: {e}")
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

# Take user input for sale details
sale_id = int(input("Enter Sale ID to update: "))
listing_id = int(input("Enter new Listing ID: "))
client_id = int(input("Enter new Client ID: "))
sale_date = input("Enter new Sale Date (YYYY-MM-DD): ")
price = int(input("Enter new Price: "))

# Call the update_sale function with user input
update_sale(connection, sale_id, listing_id, client_id, sale_date, price)

if connection.is_connected():
    connection.close()
    print("MySQL database connection closed")
