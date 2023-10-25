#!/usr/bin/python3
"""Lists all states starting with 'N' from the 'hbtn_0e_0_usa' database."""

import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    
    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute an SQL query to select all states and sort by states.id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch the results
    states = cursor.fetchall()

    # Print states starting with 'N'
    for state in states:
        if state[1].startswith("N"):
            print(state)

    # Close the cursor and the database connection
    cursor.close()
    db.close()
