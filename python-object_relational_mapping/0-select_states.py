#!/usr/bin/python3

import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    try:
        db = MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=password,
            db=database,
            port=3306
        )
        cursor = db.cursor()

        cursor.execute("SELECT * FROM states ORDER BY id ASC")

        for row in cursor.fetchall():
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error:", e)

    finally:
        if 'db' in locals() and db:
            db.close()
