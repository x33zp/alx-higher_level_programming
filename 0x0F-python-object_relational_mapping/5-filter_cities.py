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
    state_name = sys.argv[4]
    sql_query = """SELECT c.name
                FROM cities AS c
                JOIN states AS s
                ON c.state_id = s.id
                WHERE s.name = %s
                ORDER BY c.id ASC"""
    cur.execute(sql_query, (state_name,))
    rows = cur.fetchall()

    selected_cities = [row[0] for row in rows]
    print(', '.join(selected_cities))

    cur.close()
    db.close()
