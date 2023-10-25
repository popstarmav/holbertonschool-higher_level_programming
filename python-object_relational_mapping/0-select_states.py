#!/usr/bin/python3
"""List all states from the 'hbtn_0e_0_usa' database."""

import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to the 'hbtn_0e_0_usa' database
    database = MySQLdb.connect(
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
    )
    cursor = database.cursor()

    # Execute the SQL query to select all states
    cursor.execute("SELECT * FROM states")

    # Fetch and print the states
    states = cursor.fetchall()
    for state in states:
        print(state)
