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
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
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


if __name__ == '__main__' and len(sys.argv) == 4:
    username, password, database = sys.argv[1:4]
    list_states(username, password, database)
