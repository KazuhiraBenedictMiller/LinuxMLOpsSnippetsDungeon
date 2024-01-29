# Module Imports
import mariadb
import sys
import pandas as pd

def ConnectMariaDB():
    # Connect to MariaDB Platform
    try:
        connection = mariadb.connect(
            user=YOUR_MARIADB_USER,
            password=YOUR_MARIADB_PASSWORD,
            host=DB_IP_HOST,
            port=3306,
            database=YOUR_MARIADB_DATABASE
        )
        
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

    # Get Cursor
    cursor = connection.cursor()
    
    return cursor, connection


if __name__ == "__main__":
    cur, con = ConnectMariaDB()
    
    MariaDB_TableName = "TestTable"
    
    cur.execute(f'CREATE TABLE IF NOT EXISTS {MariaDB_TableName} (Date DATETIME PRIMARY KEY NOT NULL, Close DOUBLE)')
    
    for i in SOME_LIST:
        cur.execute(
        f'INSERT {MariaDB_TableName} VALUES (?, ?)',  
        (i[0], i[1]))
    
    conn.commit()
    
    #Check Inserted Data 
    cur.execute(f'SELECT * FROM {MariaDB_TableName}')

    checkdf = pd.DataFrame(data = [x for x in cur], columns = ["Date", "Close"])
    print(checkdf)

