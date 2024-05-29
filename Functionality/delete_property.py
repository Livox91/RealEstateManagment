import mysql.connector

def delete_property(property_id):
    # Database connection parameters
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

        # ----------------- if the property exists
        cursor.execute("SELECT * FROM property WHERE Property_id = %s", (property_id,))
        property_data = cursor.fetchone()
        if property_data:
            # ---------------references in listing table
            cursor.execute("SELECT * FROM listing WHERE Property_id = %s", (property_id,))
            listing_data = cursor.fetchall()
            if listing_data:
                print(f"Property ID {property_id} is referenced in the listing table. Please delete these references first.")
                return
            cursor.execute("DELETE FROM property WHERE Property_id = %s", (property_id,))
            connection.commit()
            print(f"Property with ID {property_id} has been successfully deleted.")
        else:
            print(f"Property with ID {property_id} does not exist.")

        cursor.close()
        connection.close()

    except mysql.connector.Error as err:
        print(f"Error: {err}")
