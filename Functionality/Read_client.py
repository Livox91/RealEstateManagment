import mysql.connector
from mysql.connector import Error

def read_clients():
    try:
        connection =mysql.connector.connect(
                    host  = "localhost",
                    port = 3306,
                    user = "root" ,
                    password = "1234",
                    database = "real_estate"
                )
        cursor = connection.cursor()
        sql_query = "SELECT * FROM client"
        cursor.execute(sql_query)
        clients = cursor.fetchall()
        cursor.close()
        return True,clients
    except Error as e:
       return False, f"Error reading clients: {e}"
    
