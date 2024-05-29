import mysql.connector

def add_agents(id,name,contact,agency_id,society_id):
    
    try:
        
        connection = mysql.connector.connect(
                host  = "localhost",
                port = 3306,
                user = "root" ,
                password = "1234",
                database = "real_estate"
            )
        cursor = connection.cursor()

        sql = "INSERT INTO agent (Agent_ID, Agent_Name, Contact,Agency_ID,Society_ID) VALUES (%s, %s, %s,%s,%s)"
        val = (id,name,contact,agency_id,society_id)

        cursor.execute(sql, val)
        connection.commit()

        cursor.close()
        connection.close()

        print("Agent added successfully")

    except mysql.connector.Error as err:
        print(f"Error: {err}")


