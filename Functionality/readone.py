import mysql.connector
from mysql.connector import Error

def read(table, record_id):
     try:
        db_connection=  mysql.connector.connect(
                    host  = "localhost",
                    port = 3306,
                    user = "root" ,
                    password = "1234",
                    database = "real_estate"
                )
        cursor = db_connection.cursor()
        query = f"SELECT * FROM {table} WHERE {table}_ID = %s"
        cursor.execute(query, (record_id,))
        result = cursor.fetchone()
        cursor.close()
        if result:
            return True, result
        else:
            return False, f"{table.capitalize()} not found."
     except Error as e:
        return False, f"Error reading {table} record: {e}"