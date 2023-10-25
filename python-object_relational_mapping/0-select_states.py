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
if __name__ == "__main__":
    # Connect to the MySQL database
    conn = MySQLdb.connect(
            host="localhost", 
            port=3306, charset="utf8",
            user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()

    # Execute the query to fetch states sorted by ID
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    query_rows = cur.fetchall()

    # Print the query results
    for row in query_rows:
        print(row)

    # Close the cursor and the database connection
    cur.close()
    conn.close()
