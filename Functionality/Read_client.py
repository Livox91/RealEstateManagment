import mysql.connector
from mysql.connector import Error

def read_clients(connection):
    try:
        cursor = connection.cursor()
        sql_query = "SELECT * FROM client"
        cursor.execute(sql_query)
        clients = cursor.fetchall()
        return clients
    except Error as e:
        print(f"Error reading clients: {e}")
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
        clients = read_clients(connection)
        if clients:
            print("Client_ID\tClient_Name\tContact")
            for client in clients:
                print("\t".join(str(attr) for attr in client))
        else:
            print("No clients found.")
except Error as e:
    print(f"Error connecting to MySQL database: {e}")
finally:
    if connection.is_connected():
        connection.close()
        print("MySQL database connection closed")
