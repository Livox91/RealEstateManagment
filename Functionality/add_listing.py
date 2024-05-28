import mysql.connector
from datetime import datetime

def add_listing():
   
    host = "localhost"
    user = "root"
    password = "Manahil18!"
    database = "real_estate"

    try:
        # --------------------Connect to the database
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        cursor = connection.cursor()
        
        # ------------------------validating property_id
        while True:
            property_id = input("Enter Property ID: ")
            cursor.execute("SELECT COUNT(*) FROM property WHERE Property_id = %s", (property_id,))
            if cursor.fetchone()[0] > 0:
                break
            else:
                print("Property ID does not exist. Please enter a valid Property ID.")
        
        # ---------------------validate agent_id
        while True:
            agent_id = input("Enter Agent ID: ")
            cursor.execute("SELECT COUNT(*) FROM agent WHERE Agent_id = %s", (agent_id,))
            if cursor.fetchone()[0] > 0:
                break
            else:
                print("Agent ID does not exist. Please enter a valid Agent ID.")
        
        # ------------------- input values from the user
        listing_id = input("Enter Listing ID: ")
        listing_date = input("Enter Listing Date (YYYY-MM-DD): ")

        # ----------------------Validate listing_date
        try:
            datetime.strptime(listing_date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
            return

        # ------------------------------SQL query
        sql = "INSERT INTO listing (Listing_id, Property_id, Agent_id, Listing_date) VALUES (%s, %s, %s, %s)"
        val = (listing_id, property_id, agent_id, listing_date)
        
        # ---------------Execute the SQL query
        cursor.execute(sql, val)
        
      
        connection.commit()
        cursor.close()
        connection.close()
        
        print("Listing added successfully")
    
    except mysql.connector.Error as err:
        print(f"Error: {err}")

# --------------Calling the add_listing function
add_listing()
