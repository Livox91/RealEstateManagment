import mysql.connector

def delete_agency(agency_id):
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

        # -----------if the agency exists or not
        cursor.execute("SELECT * FROM agency WHERE Agency_Id = %s", (agency_id,))
        agency_data = cursor.fetchone()
        if agency_data:
            # -------------- for references in the agent table
            cursor.execute("SELECT * FROM agent WHERE agency_id = %s", (agency_id,))
            agent_data = cursor.fetchone()
            if agent_data:
                # ---------------if Agency is referenced in the agent table
                print(f"Cannot delete Agency with ID {agency_id} because it is referenced in the agent table. Please delete the related agents first.")
            else:
                cursor.execute("DELETE FROM agency WHERE Agency_Id = %s", (agency_id,))
                connection.commit()
                print(f"Agency with ID {agency_id} has been successfully deleted.")
        else:
            # -----------------Agency does not exist
            print(f"Agency with ID {agency_id} does not exist.")
        cursor.close()
        connection.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
agency_id_to_delete = input("Enter the Agency ID to delete: ")
delete_agency(agency_id_to_delete)
