import mysql.connector

def add_client(id,name,contact):
    try:
        
        connection = mysql.connector.connect(
                host  = "localhost",
                port = 3306,
                user = "root" ,
                password = "1234",
                database = "real_estate"
            )
       
        cursor = connection.cursor()

      
        sql = "INSERT INTO client(Client_id, Client_Name, Contact) VALUES (%s, %s, %s)"
        val = (id, name, contact)

        cursor.execute(sql, val)

     
        connection.commit()

        cursor.close()
        connection.close()

        print("Client added successfully")

    except mysql.connector.Error as err:
        print(f"Error: {err}")



