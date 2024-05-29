import mysql.connector
def validate_society(society_id, cursor):
    cursor.execute("SELECT COUNT(*) FROM society WHERE Society_id = %s", (society_id,))
    if cursor.fetchone()[0] > 0:
        return True
    else:
        print("Society ID does not exist. Please enter a valid Society ID.")
        return False

def add_property(property_id, title, area_size, location, society_id, property_type, specific_id=None):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="1234",
            database="real_estate"
        )
        cursor = connection.cursor()

        if not validate_society(society_id, cursor):
            return

        sql = """
        INSERT INTO property 
        (Property_ID, Title, Area_Size, Location, Society_Id, Type, Plot_ID, House_ID, Apartment_ID, Shop_ID) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        
        val = (property_id, title, area_size, location, society_id, property_type,
               specific_id if property_type == 'plot' else None,
               specific_id if property_type == 'house' else None,
               specific_id if property_type == 'apartment' else None,
               specific_id if property_type == 'shop' else None)

        cursor.execute(sql, val)
        connection.commit()
        cursor.close()
        connection.close()

        print("Property added successfully")

    except mysql.connector.Error as err:
        print(f"Error: {err}")