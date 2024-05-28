import mysql.connector
from mysql.connector import Error

def read_agents(connection):
    try:
        cursor = connection.cursor()
        sql_query = "SELECT * FROM agent"
        cursor.execute(sql_query)
        agents = cursor.fetchall()
        return agents
    except Error as e:
        print(f"Error reading agents: {e}")
    finally:
        cursor.close()

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Manahil18!",
        database="real_estate")
    if connection.is_connected():
        print("Connected to MySQL database")
        agents = read_agents(connection)
        if agents:
            print("Agent_ID\tAgent_Name\tContact\t\tAgency_ID\tSociety_ID")
            for agent in agents:
                print("\t".join(str(attr) for attr in agent))
        else:
            print("No agents found.")
except Error as e:
    print(f"Error connecting to MySQL database: {e}")
finally:
    if connection.is_connected():
        connection.close()
        print("MySQL database connection closed")
