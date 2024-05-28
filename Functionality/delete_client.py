import mysql.connector

def delete_client(client_id):
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

        cursor.execute("SELECT * FROM client WHERE client_id = %s", (client_id,))
        client_data = cursor.fetchone()
        if client_data:
    
            cursor.execute("DELETE FROM client WHERE client_id = %s", (client_id,))
            connection.commit()
            print(f"Client with ID {client_id} has been successfully deleted.")
        else:
         
            print(f"Client with ID {client_id} does not exist.")

        cursor.close()
        connection.close()

    except mysql.connector.Error as err:
        print(f"Error: {err}")
client_id_to_delete = input("Enter the Client ID to delete: ")
delete_client(client_id_to_delete)
