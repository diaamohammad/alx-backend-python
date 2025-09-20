#!/usr/bin/env python3
"""
Context manager that executes a query and manages DB connection.
"""

import sqlite3


class ExecuteQuery:
    def __init__(self, db_name, query, params=None):
        self.db_name = db_name
        self.query = query
        self.params = params if params else ()
        self.conn = None
        self.cursor = None
        self.result = None

    def __enter__(self):
        # open connection and execute the query
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute(self.query, self.params)
        self.result = self.cursor.fetchall()
        return self.result

    def __exit__(self, exc_type, exc_value, traceback):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
        # Don't suppress exceptions if any
        return False


if __name__ == "__main__":
    query = "SELECT * FROM users WHERE age > ?"
    params = (25,)
    # Example usage
    with ExecuteQuery("db.sqlite3", query, params) as result:
        for row in result:
            print(row)
