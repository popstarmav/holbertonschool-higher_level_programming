#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa."""

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         password=sys.argv[2], db=sys.argv[3], port=3306)
    c = db.cursor()
    c.execute("SELECT * FROM states ORDER by id ASC")
    data = cursor.fetchall()
    for row in data:
        print(row)
    cursor.close()
    dbclose
