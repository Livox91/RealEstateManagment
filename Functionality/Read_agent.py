import mysql.connector
from mysql.connector import Error

def read_agents():
    try:

        connection =  mysql.connector.connect(
                host  = "localhost",
                port = 3306,
                user = "root" ,
                password = "1234",
                database = "real_estate"
            )
        cursor = connection.cursor()
        sql_query = "SELECT * FROM agent"
        cursor.execute(sql_query)
        agents = cursor.fetchall()
        cursor.close()
        return True,agents
    except Error as e:
       return False, f"Error reading agents: {e}"
    

