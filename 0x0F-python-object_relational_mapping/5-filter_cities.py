#!/usr/bin/python3
"""
This script lists all cities from the database hbtn_0e_4_usa
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

    sql_query = "SELECT cities.name FROM cities INNER JOIN states\
                  ON states.id=cities.state_id\
                      WHERE states.name='{}'".format(state_name)

    cur.execute(sql_query)

    query_rows = cur.fetchall()
    tmp = list(row[0] for row in query_rows)
    print(*tmp, sep=", ")

    cur.close()
    conn.close()
