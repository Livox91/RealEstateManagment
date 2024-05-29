import mysql.connector

def add_agency(name ,id):
    try:
       
        connection =  mysql.connector.connect(
                host  = "localhost",
                port = 3306,
                user = "root" ,
                password = "1234",
                database = "real_estate"
            )

        # --------------------Cursor object
        cursor = connection.cursor()

        # ---------------- SQL query
        sql = "INSERT INTO agency (Agency_Id, Agency_Name) VALUES (%s, %s)"
        val = (id, name)

        # -----------------Execution of the query
        cursor.execute(sql, val)
        connection.commit()
        cursor.close()
        connection.close()

        print("Agency added successfully")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

