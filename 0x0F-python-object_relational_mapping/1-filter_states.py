#!/usr/bin/python3
""" filter all states
"""
if __name__ == "__main__":
    import sys
    import MySQLdb

    conn = MySQLdb.connect(user=sys.argv[1], password=sys.argv[2],
                           database=sys.argv[3])
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM states;")
    query_rows = cursor.fetchall()
    for row in query_rows:
        if row[1][0] == 'N':
            print("{}".format(row))
    cursor.close()
    conn.close()
