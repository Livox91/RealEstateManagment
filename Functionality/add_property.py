import mysql.connector

def add_property():
   
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
        property_id = input("Enter Property ID: ")
        title = input("Enter Title: ")
        area_size = input("Enter Area Size (sq.ft): ")
        location = input("Enter Location: ")

        # --------validate society_id
        while True:
            society_id = input("Enter Society ID: ")
            cursor.execute("SELECT COUNT(*) FROM society WHERE Society_id = %s", (society_id,))
            if cursor.fetchone()[0] > 0:
                break
            else:
                print("Society ID does not exist. Please enter a valid Society ID.")

        # -----------------property type
        property_type = input("Enter Property Type: ")

        # --------------------validate plot_id
        while True:
            plot_id = input("Enter Plot ID : ")
            if not plot_id:
                plot_id = None
                break
            cursor.execute("SELECT COUNT(*) FROM plot WHERE Plot_id = %s", (plot_id,))
            if cursor.fetchone()[0] > 0:
                break
            else:
                print("Plot ID does not exist. Please enter a valid Plot ID.")

        # --------------validate house_id
        while True:
            house_id = input("Enter House ID (or leave blank if not applicable): ")
            if not house_id:
                house_id = None
                break
            cursor.execute("SELECT COUNT(*) FROM house WHERE House_id = %s", (house_id,))
            if cursor.fetchone()[0] > 0:
                break
            else:
                print("House ID does not exist. Please enter a valid House ID.")

        # -------------------------validate apartment_id
        while True:
            apartment_id = input("Enter Apartment ID (or leave blank if not applicable): ")
            if not apartment_id:
                apartment_id = None
                break
            cursor.execute("SELECT COUNT(*) FROM apartment WHERE Apartment_id = %s", (apartment_id,))
            if cursor.fetchone()[0] > 0:
                break
            else:
                print("Apartment ID does not exist. Please enter a valid Apartment ID.")

        # -------------------validate shop_id
        while True:
            shop_id = input("Enter Shop ID (or leave blank if not applicable): ")
            if not shop_id:
                shop_id = None
                break
            cursor.execute("SELECT COUNT(*) FROM shops WHERE Shop_id = %s", (shop_id,))
            if cursor.fetchone()[0] > 0:
                break
            else:
                print("Shop ID does not exist. Please enter a valid Shop ID.")

        sql = """
        INSERT INTO property (`Property_id`, `Title`, `Area_Size(sq.ft)`, `Location`, `Society_id`, `Type`, `Plot_id`, `House_id`, `Apartment_id`, `Shop_id`) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        val = (property_id, title, area_size, location, society_id, property_type, plot_id, house_id, apartment_id, shop_id)

        # --------------------SQL query
        cursor.execute(sql, val)
        connection.commit()
        cursor.close()
        connection.close()

        print("Property added successfully")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

# ------------------add_property function
add_property()
