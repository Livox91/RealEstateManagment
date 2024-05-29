import mysql.connector
from mysql.connector import Error

def create(table, *args, **kwargs):
        try:
            connection = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="1234",
            database="real_estate"
            )
            with connection.cursor() as cursor:
                columns = ', '.join(kwargs.keys())
                values = ', '.join(['%s'] * len(kwargs))
                query = f"INSERT INTO {table} ({columns}) VALUES ({values})"
                cursor.execute(query, tuple(kwargs.values()))
                connection.commit()
            return True, f"{table.capitalize()} record created successfully."
        except Error as e:
            return False, f"Error creating {table} record: {e}"
