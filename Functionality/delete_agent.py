import mysql.connector

def delete_agent(agent_id):
  
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
agent_id_to_delete = input("Enter the Agent ID to delete: ")
delete_agent(agent_id_to_delete)
