import mysql.connector
from mysql.connector import Error

def update_client(connection, client_id, client_name, contact):
    try:
        cursor = connection.cursor()
        sql_query = """UPDATE client SET Client_Name = %s, Contact = %s WHERE Client_ID = %s"""
        cursor.execute(sql_query, (client_name, contact, client_id))
        connection.commit()
        print("Client updated successfully!")
    except Error as e:
        print(f"Error updating client: {e}")
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

# Take user input for client details
client_id = int(input("Enter Client ID to update: "))
client_name = input("Enter new client name: ")
contact = input("Enter new contact number: ")

# Call the update_client function with user input
update_client(connection, client_id, client_name, contact)

if connection.is_connected():
    connection.close()
    print("MySQL database connection closed")
