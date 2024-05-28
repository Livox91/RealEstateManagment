import mysql.connector

def add_agency():
    # ----------taking inputs firm users
    agency_id = input("Enter Agency ID: ")
    agency_name = input("Enter Agency Name: ")

    # ---------------connecting to database
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

        # --------------------Cursor object
        cursor = connection.cursor()

        # ---------------- SQL query
        sql = "INSERT INTO agency (Agency_Id, Agency_Name) VALUES (%s, %s)"
        val = (agency_id, agency_name)

        # -----------------Execution of the query
        cursor.execute(sql, val)
        connection.commit()
        cursor.close()
        connection.close()

        print("Agency added successfully")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

# ---------add_agency function
add_agency()
