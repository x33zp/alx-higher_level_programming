#!/usr/bin/python3
"""
This script connects to a MySQL database and fetches all rows
from the 'states' table, then prints all values in the states
table of hbtn_0e_0_usa where name matches the argument.
But this time, it is safe from MySQL injections!
"""
import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(
         host='localhost',
         user=sys.argv[1],
         passwd=sys.argv[2],
         db=sys.argv[3],
         port=3306)
    cur = db.cursor()
    state_name = sys.argv[4]
    sql_query = """SELECT * FROM states
                WHERE name LIKE %s
                ORDER BY states.id ASC"""
    cur.execute(sql_query, (state_name,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
