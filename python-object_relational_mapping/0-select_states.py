import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306
    )

    cur = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    data = cursor.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
