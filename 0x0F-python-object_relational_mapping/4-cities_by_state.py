#!/usr/bin/python3
"""
This script connects to a MySQL database and fetches all rows
from the 'states' table, then prints all the cities from the database
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
    cur.execute("""SELECT c.id, c.name, s.name
                FROM cities AS c JOIN states AS s
                ON c.state_id = s.id
                ORDER BY c.id ASC""")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()

