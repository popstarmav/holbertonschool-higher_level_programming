t_relational_mapping# cat 0-select_states.
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
    # Connect to MySQL server
    db = MySQLdb.connect(
                host='localhost',
                port=3306,
                user=username,
                passwd=password,
                db=database
        )
    cursor = db.cursor()

    # Execute SQL query to fetch all states sorted by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch and print query results
    for row in cursor.fetchall():
        print(row)

    # Close the database connection
    db.close()

if __name__ == '__main__':
    if len(sys.argv) == 4:
        username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
        list_states(username, password, database)
