#!/usr/bin/python3
"""
This script takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    conn = MySQLdb.connect(host="localhost",
                           user=username, passwd=password,
                           database=db_name, port=3306)

    cur = conn.cursor()
    cur.execute(f"SELECT * FROM states WHERE name={state_name}")

    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    cur.close()
    conn.close()
