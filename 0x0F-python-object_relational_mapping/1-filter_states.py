#!/usr/bin/python3
""" ists all states with a name starting with N
(upper N) from the database hbtn_0e_0_usa: """

import MySQLdb
import sys

if __name__ == '__main__':
    con = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = con.cursor()
    cur.execute("select * from states where like 'N%';")
    for i in cur.fetchall():
        print(i)
