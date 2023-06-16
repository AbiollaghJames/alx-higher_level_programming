#!/usr/bin/python3

"""
a script that lists all states from the database hbtn_0e_0_usa
The script should take 3 arguments: mysql username, mysql password and database name (no argument validation needed)

"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    pasword = sys.argv[2]
    db_name = sys.argv[3]

    conn = MySQLdb.connect(host="localhost", user="username", passwd="password", db="db_name")
    curr = conn.cursor()

    curr.execute("SELECT * FROM states")
    res = curr.fetchall()

    for row in res:
        print(row)

    curr.close()
    conn.close()

