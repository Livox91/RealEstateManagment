import mysql.connector
import Update.Update
def delete_agent():
  
    DeleteWindow = Update.Update.UpdateScreen()
    agent_id = DeleteWindow.get_id_entry_value()
    if agent_id:
        try:
            connection = mysql.connector.connect(
                        host  = "localhost",
                        port = 3306,
                        user = "root" ,
                        password = "1234",
                        database = "real_estate"
                    )
            cursor = connection.cursor()

            # -------------------if the agent exists or not
            cursor.execute("SELECT * FROM agent WHERE agent_id = %s", (agent_id,))
            agent_data = cursor.fetchone()
            if agent_data:
                # -----------------Check for references in the listing table
                cursor.execute("SELECT * FROM listing WHERE agent_id = %s", (agent_id,))
                listing_data = cursor.fetchone()
                if listing_data:
                    # -------------if Agent is referenced in the listing table
                    print(f"Cannot delete Agent with ID {agent_id} because it is referenced in the listing table. Please delete the related listings first.")
                else:
                    cursor.execute("DELETE FROM agent WHERE agent_id = %s", (agent_id,))
                    connection.commit()
                    print(f"Agent with ID {agent_id} has been successfully deleted.")
            else:
                #-----------if Agent does not exist
                print(f"Agent with ID {agent_id} does not exist.")
            cursor.close()
            connection.close()

        except mysql.connector.Error as err:
            print(f"Error: {err}")
