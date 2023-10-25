#!/usr/bin/python3
"""List all states from the hbtn_0e_0_usa database."""

import sys
import MySQLdb

def list_states(username, password, database):
    """List all states from the database.

    Args:
        username (str): MySQL username
        password (str): MySQL password
        database (str): MySQL database name
    """
    try:
        # Connect to MySQL server
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )
        cursor = db.cursor()

        # Execute the SQL query to fetch all states sorted by ID
        cursor.execute("SELECT * FROM states ORDER BY id ASC")

        results = cursor.fetchall()
        for state in results:
            print(state)

        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    if len(sys.argv) == 4:
        username, password, database = sys.argv[1:4]
        list_states(username, password, database_name)

