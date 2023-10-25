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
        conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )
        cursor = conn.cursor()

        # Execute the SQL query to fetch all states sorted by ID
        cursor.execute("SELECT * FROM states ORDER BY id ASC")

        # Fetch and print the results
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print(f"Error: {e}")

    finally:
        # Close the cursor and the database connection
        cursor.close()
        conn.close()


if __name__ == '__main__' and len(sys.argv) == 4:
    username, password, database = sys.argv[1:4]
    list_states(username, password, database)
