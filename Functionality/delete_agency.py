import mysql.connector
import Update.Update
def delete_agency():
    DeleteWindow = Update.Update.UpdateScreen()
    agency_id = DeleteWindow.get_id_entry_value()
    if agency_id:
        try:
            connection = mysql.connector.connect(
                    host  = "localhost",
                    port = 3306,
                    user = "root" ,
                    password = "1234",
                    database = "real_estate"
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

