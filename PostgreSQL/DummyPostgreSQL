import psycopg2
import pandas as pd
import sys

def ConnectPostgreSQL():
    # Connect to PostgreSQL
    try:
        connection = psycopg2.connect(
            user="YOUR_PostgreSQL_User",
            password="YOUR_PostgreSQL_Password",
            host="localhost",
            port="5432",
            database="YOUR_PostgreSQL_Database"
        )
        return connection

    except psycopg2.Error as e:
        print(f"Error connecting to PostgreSQL: {e}")
        sys.exit(1)

if __name__ == "__main__":
    connection = ConnectPostgreSQL()

    # Example data for SOME_LIST
    SOME_LIST = [("2024-02-15 10:00:00", 25.5),
                 ("2024-02-15 11:00:00", 30.2)]

    if connection:
        # Create cursor
        cursor = connection.cursor()

        # Create table if not exists
        cursor.execute('''CREATE TABLE IF NOT EXISTS TestTable (
                            Date TIMESTAMP PRIMARY KEY NOT NULL,
                            Close FLOAT
                          )''')

        # Insert data into PostgreSQL
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
