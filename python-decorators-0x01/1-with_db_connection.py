import sqlite3
from functools import wraps

def with_db_connection(func):
    @wraps(func)
    def wrapper(*args,**kwargs):

        conn = sqlite3.connect('users.db')
        result = func(conn, *args, **kwargs)
        conn.close()
        return result
    return wrapper

@with_db_connection
def get_user_by_id(conn, user_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,)) 
    return cursor.fetchone() 

user = get_user_by_id(user_id=1)
print(user)
