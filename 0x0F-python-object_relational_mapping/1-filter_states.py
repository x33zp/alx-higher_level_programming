#!/usr/bin/python3
"""
This script connects to a MySQL database and fetches all rows
from the 'states' table, then prints all states with a
name starting with N (upper N) from the database
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    db_connect = db.connect(host="localhost", port=3306,
                            user=argv[1], passwd=argv[2], db=argv[3])
    db_cursor = db_connect.cursor()

    db_cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' \
                ORDER BY states.id ASC")

    rows_selected = db_cursor.fetchall()

    for row in rows_selected:
        print(row)
