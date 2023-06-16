#!/usr/bin/python3

"""
 a script that takes in an argument and displays all values
 in the states table of hbtn_0e_0_usa where name matches the argument
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
    name_searched = sys.argv[4]
    curr = db.cursor()
    curr.execute("SELECT * FROM states WHERE \
            name = BINARY '{:s}' ORDER BY id ASC;".format(name_searched))
    res = curr.fetchall()

    for row in res:
        print(row)

    curr.close()
    db.close()
