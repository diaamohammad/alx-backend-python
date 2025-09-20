#!/usr/bin/env python3
"""
Custom class-based context manager for Database connection
"""

import sqlite3


class DatabaseConnection:
    def __init__(self, db_name):
        """Initialize with database name"""
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def __enter__(self):
        """Open connection and return cursor"""
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_value, traceback):
        """Close cursor and connection"""
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
        # Do not suppress exceptions
        return False


if __name__ == "__main__":
    # Example usage
    with DatabaseConnection("db.sqlite3") as cursor:
        cursor.execute("SELECT * FROM users")
        results = cursor.fetchall()
        for row in results:
            print(row)
