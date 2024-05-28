import mysql.connector

def add_society():
    
    society_id = input("Enter Society ID: ")
    city = input("Enter City: ")
    no_of_houses = input("Enter Number of Houses: ")
    no_of_plots = input("Enter Number of Plots: ")
    avg_house_price = input("Enter Average House Price: ")
    avg_plot_price = input("Enter Average Plot Price: ")

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

        sql = "INSERT INTO society (Society_id, city, no_of_houses, no_of_plots, avg_house_price, avg_plot_price) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (society_id, city, no_of_houses, no_of_plots, avg_house_price, avg_plot_price)

        cursor.execute(sql, val)

        connection.commit()
        cursor.close()
        connection.close()

        print("Society added successfully")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
add_society()
