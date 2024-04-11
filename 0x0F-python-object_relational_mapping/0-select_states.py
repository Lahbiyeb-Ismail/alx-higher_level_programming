#!/usr/bin/python3

import MySQLdb
import sys

username = sys.argv[1]
password = sys.argv[2]
db_name = sys.argv[3]

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost",
                           user=username, passwd=password,
                           database=db_name, port=3306)

    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
