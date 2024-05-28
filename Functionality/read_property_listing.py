import mysql.connector

def retrieve_property_by_listing_id():
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

            # Take Listing_ID input from user
            listing_id = int(input("Enter the Listing_ID: "))

            # Prepare SQL query to select property by Listing_ID from sale table
            sale_query = "SELECT * FROM sale WHERE Listing_ID = %s"
            cursor.execute(sale_query, (listing_id,))
            sale_data = cursor.fetchone()

            # Prepare SQL query to select property by Listing_ID from rental table
            rental_query = "SELECT * FROM rental WHERE Listing_ID = %s"
            cursor.execute(rental_query, (listing_id,))
            rental_data = cursor.fetchone()

            if sale_data:
                print("Property found in sale table:")
                print(sale_data)
            elif rental_data:
                print("Property found in rental table:")
                print(rental_data)
            else:
                print("No property found for Listing_ID:", listing_id)

    except mysql.connector.Error as e:
        print("Error retrieving property data:", e)

    finally:
        # Close database connection
        if conn.is_connected():
            cursor.close()
            conn.close()

# Call the function
retrieve_property_by_listing_id()
