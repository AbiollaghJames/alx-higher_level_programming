#!/usr/bin/python3

"""
a script that takes in arguments and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections!
"""

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
    curr = db.cursor()
    name_searched = sys.argv[4]
    querry = "SELECT * FROM states WHERE name = %s"

    curr.execute(querry, (name_searched, ))
    res = curr.fetchall()

    for row in res:
        print(row)

    curr.close()
    db.close()
