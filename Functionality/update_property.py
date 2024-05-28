import mysql.connector
from mysql.connector import Error

def update_property(connection, property_id, title, area_size, location, society_id, property_type, plot_id, house_id, apartment_id, shop_id):
    try:
        cursor = connection.cursor()
        sql_query = """UPDATE property SET Title = %s, `Area_Size (sq.ft)` = %s, Location = %s, Society_Id = %s, Type = %s, Plot_ID = %s, House_ID = %s, Apartment_ID = %s, Shop_ID = %s WHERE Property_ID = %s"""
        cursor.execute(sql_query, (title, area_size, location, society_id, property_type, plot_id, house_id, apartment_id, shop_id, property_id))
        connection.commit()
        print("Property updated successfully!")
    except Error as e:
        print(f"Error updating property: {e}")
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

# Take user input for property details
property_id = int(input("Enter Property ID to update: "))
title = input("Enter new title: ")
area_size = input("Enter new area size (sq.ft): ")
location = input("Enter new location: ")
society_id = int(input("Enter new Society ID: "))
property_type = input("Enter new property type (House/Plot): ")
plot_id = int(input("Enter new Plot ID (or enter 0 if not applicable): "))
house_id = int(input("Enter new House ID (or enter 0 if not applicable): "))
apartment_id = int(input("Enter new Apartment ID (or enter 0 if not applicable): "))
shop_id = int(input("Enter new Shop ID (or enter 0 if not applicable): "))

# Call the update_property function with user input
update_property(connection, property_id, title, area_size, location, society_id, property_type, plot_id, house_id, apartment_id, shop_id)

if connection.is_connected():
    connection.close()
    print("MySQL database connection closed")

