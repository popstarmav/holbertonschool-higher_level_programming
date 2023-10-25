#!/usr/bin/python3
import MySQLdb
import sys

def list_states(username, password, database):
    try:
        # Connect to the MySQL database
        db = MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=password,
            db=database,
            port=3306
        )

        # Create a cursor object to interact with the database
        cursor = db.cursor()

        # Execute an SQL query to select all data from the "states" table
        cursor.execute("SELECT * FROM states")

        # Fetch all the rows from the query result
        rows = cursor.fetchall()

        return rows

    except MySQLdb.Error as e:
        print("MySQL Error:", e)
        return None

    finally:
        if 'db' in locals() and db:
            db.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    rows = list_states(username, password, database)

    if rows:
        for row in rows:
            print(row)
