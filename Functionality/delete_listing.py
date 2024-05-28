import mysql.connector

def delete_listing(listing_id):
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

        # ------------listing exists or not
        cursor.execute("SELECT * FROM listing WHERE listing_id = %s", (listing_id,))
        listing_data = cursor.fetchone()
        if listing_data:
            # --------------if it has refrences in rental table
            cursor.execute("SELECT * FROM rental WHERE listing_id = %s", (listing_id,))
            rental_data = cursor.fetchall()
            if rental_data:
                print(f"  Please delete listing id {listing_id} from rental table first.")
                return

            # ----------if it has references in sale table
            cursor.execute("SELECT * FROM sale WHERE listing_id = %s", (listing_id,))
            sale_data = cursor.fetchall()
            if sale_data:
                print(f"Please delete listing id {listing_id} from sales table first..")
                return

            # ----------deleting the listing
            cursor.execute("DELETE FROM listing WHERE listing_id = %s", (listing_id,))
            connection.commit()
            print(f"Listing with ID {listing_id} has been successfully deleted.")
        else:
            # --------------if Listing does not exist
            print(f"Listing with ID {listing_id} does not exist.")
        cursor.close()
        connection.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
listing_id_to_delete = input("Enter the Listing ID to delete: ")
delete_listing(listing_id_to_delete)
