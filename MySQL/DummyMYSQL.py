import mysql.connector
import pandas as pd
import sys

def ConnectMySQL():
    # Connect to MySQL
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="YOUR_MySQL_User",
            password="YOUR_MySQL_Password",
            database="YOUR_MySQL_Database"
        )
        return connection
      
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL: {e}")
        sys.exit(1)

if __name__ == "__main__":
    connection = ConnectMySQL()

    # Example data for SOME_LIST
    SOME_LIST = [("2024-02-15 10:00:00", 25.5),
                 ("2024-02-15 11:00:00", 30.2)]

    if connection:
        # Create cursor
        cursor = connection.cursor()

        # Create table if not exists
        cursor.execute('''CREATE TABLE IF NOT EXISTS TestTable (
                            Date DATETIME PRIMARY KEY NOT NULL,
                            Close DOUBLE
                          )''')

        # Insert data into MySQL
        for data in SOME_LIST:
            cursor.execute('''INSERT INTO TestTable (Date, Close)
                              VALUES (%s, %s)''', data)

        # Commit changes
        connection.commit()

        # Check Inserted Data
        cursor.execute("SELECT * FROM TestTable")
        check_data = cursor.fetchall()
        checkdf = pd.DataFrame(check_data, columns=["Date", "Close"])
        print(checkdf)

        # Close cursor and connection
        cursor.close()
        connection.close()
