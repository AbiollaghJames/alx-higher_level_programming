#!/usr/bin/python3

"""
a script that lists all states from the database hbtn_0e_0_usa
The script should take 3 arguments: mysql username, mysql password and database name (no argument validation needed)

"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)

    curr = db.curso()
    curr.execute("SELECT * FROM states ORDER BY id ASC")

    res = curr.fetchall()
    for row in res:
        print(row)

    curr.close()
    db.close()
