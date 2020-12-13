#!/usr/bin/python3
""" Query SQL from python
"""
if __name__ == "__main__":
    import sys
    import MySQLdb

    conn = MySQLdb.connect(user=sys.argv[1], password=sys.argv[2],
                           database=sys.argv[3])
    cursor = conn.cursor()
    cursor.execute("SELECT c.id, c.name, s.name\
                    FROM cities AS c\
                    JOIN states AS s \
                    ON c.state_id=s.id ORDER BY s.id;")
    query_rows = cursor.fetchall()
    for row in query_rows:
        print("{}".format(row))
    cursor.close()
    conn.close()
