#!/usr/bin/python3
""" Select all database states
"""


if __name__ == "__main__":
    import sys
    import MySQLdb

    conn = MySQLdb.connect(user=sys.argv[1], password=sys.argv[2],
                           database=sys.argv[3])
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id;")
    query_rows = cursor.fetchall()
    for row in query_rows:
        print("{}".format(row))
    cursor.close()
    conn.close()
