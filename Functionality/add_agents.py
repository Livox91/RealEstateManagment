import mysql.connector

def add_client():
    # Retrieve input values from the user
    client_id = input("Enter Client ID: ")
    client_name = input("Enter Client Name: ")
    contact = input("Enter Contact Number: ")

    host = "localhost"
    user = "root"
    password = "Manahil18!"
    database = "real_estate"

    try:
        
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        cursor = connection.cursor()

        sql = "INSERT INTO client (Client_id, Client_Name, Contact) VALUES (%s, %s, %s)"
        val = (client_id, client_name, contact)

        cursor.execute(sql, val)
        connection.commit()

        cursor.close()
        connection.close()

        print("Client added successfully")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

add_client()
