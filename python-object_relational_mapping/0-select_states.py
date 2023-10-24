#!/usr/bin/python3
"""List all states from a MySQL database."""

import sys
import MySQLdb

def list_states(username, password, database):
    """List all states from the given MySQL database.

    Args:
        username (str): MySQL username
        password (str): MySQL password
        database (str): MySQL database name
    """
    # Connect to MySQL server
    # Connect to MySQL server
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cursor = db.cursor()


    # Execute SQL query to fetch all states
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch and print query results
    for row in cursor.fetchall():
        print(row)

    # Close the database connection
    db.close()

# Example usage
if __name__ == '__main__':
    username, password, database = sys.argv[1:4]
    list_states(username, password, database)
