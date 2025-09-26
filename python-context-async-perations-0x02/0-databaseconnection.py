
import sqlite3


class databaseconnection():
    
    def __init__(self,db_name):

        self.db_name = db_name
        self.conn = None

    def __enter__(self):

        self.conn = sqlite3.connect(self.db_name)
        return self.conn
    
    def __exit__(self, exc_type, exc_value, traceback):

        if self.conn:
            self.conn.close()

with databaseconnection('db_users') as conn:

    cursor = conn.cursor()
    cursor.execute('select * from users')
    result = cursor.fetchall()

for row in result:
    print (row)



