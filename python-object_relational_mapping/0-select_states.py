#!/usr/bin/python3
"""List all states from the hbtn_0e_0_usa database."""

import MySQLdb
import sys

def list_states(username, password, database):
    """List all states from the database.

    Args:
        username (str): MySQL username
        password (str): MySQL password
        database (str): MySQL database name
    """
    try:
        # Connect to the MySQL database
        db = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306
        )
        cursor = db.cursor()

        # Execute the SQL query to fetch all states
        cursor.execute("SELECT * FROM states")

        # Fetch and print the results
        rows = cursor.fetchall()
        for row in rows:
            print(row)


    except MySQLdb.Error as e:
        print(f"Error: {e}")

    finally:
        # Close the cursor and the database connection
        cursor.close()
        db.close()
