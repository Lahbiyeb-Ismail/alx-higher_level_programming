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

    conn = MySQLdb.connect(host="localhost",
                           user=username, passwd=password,
                           database=db_name, port=3306)

    cur = conn.cursor()

    sql_query = "SELECT cities.id, cities.name, state.name\
                FROM cities INNER JOIN states ON cities.state_id = states.id"

    cur.execute(sql_query)

    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    cur.close()
    conn.close()
