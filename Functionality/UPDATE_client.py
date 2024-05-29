import mysql.connector
from mysql.connector import Error

def update_client(client_id, client_name, contact):
    try:
        connection = mysql.connector.connect(
                    host  = "localhost",
                    port = 3306,
                    user = "root" ,
                    password = "1234",
                    database = "real_estate"
                )
        if connection.is_connected():
            print("Connected to MySQL database")
    except Error as e:
        print(f"Error connecting to MySQL database: {e}")

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

