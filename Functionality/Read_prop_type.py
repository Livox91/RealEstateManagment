import mysql.connector

def read_property_by_type():
    try:
        # Connect to MySQL database
        conn = mysql.connector.connect(
            host="localhost",
        user="root",
        password="Manahil18!",
        database="real_estate"
        )

        if conn.is_connected():
            cursor = conn.cursor(dictionary=True)

            # Take property type input from user
            property_type = input("Enter the Property Type (House/Plot): ")

            # Prepare SQL query to select property by type
            query = "SELECT * FROM property WHERE Type = %s"

            # Execute the query
            cursor.execute(query, (property_type,))

            # Fetch the results
            property_data = cursor.fetchall()

            if property_data:
                print("Properties Found:")
                for property in property_data:
                    print(property)
            else:
                print("No properties found for type:", property_type)

    except mysql.connector.Error as e:
        print("Error reading properties:", e)

    finally:
        # Close database connection
        if conn.is_connected():
            cursor.close()
            conn.close()

# Call the function
read_property_by_type()
