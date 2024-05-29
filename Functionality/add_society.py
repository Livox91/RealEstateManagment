import mysql.connector

def add_society(id,city,no_houses,no_plot,housep,plotp, name):
    try:
        connection =mysql.connector.connect(
                host  = "localhost",
                port = 3306,
                user = "root" ,
                password = "1234",
                database = "real_estate"
            )

      
        cursor = connection.cursor()

        sql = "INSERT INTO society (Society_id, city, no_of_houses, no_of_plots, avg_house_price, avg_plot_price,Society_name) VALUES (%s, %s, %s, %s, %s, %s,%s)"
        val = (id, city, no_houses, no_plot, housep, plotp,name)

        cursor.execute(sql, val)

        connection.commit()
        cursor.close()
        connection.close()

        print("Society added successfully")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

