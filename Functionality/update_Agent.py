import mysql.connector
from mysql.connector import Error

def update_agent(agent_id, agent_name, contact, agency_id, society_id):
    try:
        connection =mysql.connector.connect(
                    host  = "localhost",
                    port = 3306,
                    user = "root" ,
                    password = "1234",
                    database = "real_estate"
                )
        cursor = connection.cursor()

        # Check if agency_id exists
        cursor.execute("SELECT * FROM agency WHERE Agency_ID = %s", (agency_id,))
        if not cursor.fetchone():
            print("Error: Agency_ID does not exist.")
            return

        # Check if society_id exists
        cursor.execute("SELECT * FROM society WHERE Society_ID = %s", (society_id,))
        if not cursor.fetchone():
            print("Error: Society_ID does not exist.")
            return

        # Update the agent record
        sql_query = """UPDATE agent SET Agent_Name = %s, Contact = %s, Agency_ID = %s, Society_ID = %s WHERE Agent_ID = %s"""
        cursor.execute(sql_query, (agent_name, contact, agency_id, society_id, agent_id))
        connection.commit()
        print("Agent updated successfully!")
    except Error as e:
        print(f"Error updating agent: {e}")
    finally:
        cursor.close()
