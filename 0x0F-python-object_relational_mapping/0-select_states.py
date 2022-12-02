#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa: """

import sys
import MySQLdb

if __name__ == '__main__':
            con = MySQLdb.connect("localhost",sys.argv[1], sys.argv[2], sys.argv[3])
            cur = con.cursor()
            command = cur.execute("select * from states")
            for i in command:
                print(i)



