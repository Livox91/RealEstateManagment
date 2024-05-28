import mysql.connector
from mysql.connector import Error

def update_agent(connection, agent_id, agent_name, contact, agency_id, society_id):
    try:
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

try:
    connection = mysql.connector.connect(
         host="localhost",
        user="root",
        password="Manahil18!",
        database="real_estate"
    )
    if connection.is_connected():
        print("Connected to MySQL database")
except Error as e:
    print(f"Error connecting to MySQL database: {e}")

# Take user input for agent details
agent_id = int(input("Enter Agent ID to update: "))
agent_name = input("Enter new agent name: ")
contact = input("Enter new contact number: ")
agency_id = int(input("Enter new Agency ID: "))
society_id = int(input("Enter new Society ID: "))

# Call the update_agent function with user input
update_agent(connection, agent_id, agent_name, contact, agency_id, society_id)

if connection.is_connected():
    connection.close()
    print("MySQL database connection closed")
