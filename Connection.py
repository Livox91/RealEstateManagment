import mysql.connector
from mysql.connector import Error


def addRecordtoTable(table, *args, **kwargs):
        try:
            db = mysql.connector.connect(
                host  = "localhost",
                port = 3306,
                user = "root" ,
                password = "1234",
                database = "real_estate"
            )
            if db.is_connected():
                 print("connected")
            with db.cursor() as cursor:
                columns = ', '.join(kwargs.keys())
                values = ', '.join(['%s'] * len(kwargs))
                query = f"INSERT INTO {table} ({columns}) VALUES ({values})"
                cursor.execute(query, tuple(kwargs.values()))
                db.commit()
            return True, f"{table.capitalize()} record created successfully."
        except Error as e:
            return False, f"Error creating {table} record: {e}"

