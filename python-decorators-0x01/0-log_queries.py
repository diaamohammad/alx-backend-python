import sqlite3
from functools import wraps

def log_queries(func):
    @wraps(func)
    def wrapper(*args,**kwargs):

        query = args[0] if args  else kwargs.get('query','no query provieded')
        print(f'excuting query: {query}')
        result = func(*args,**kwargs)
        return result
    return wrapper


@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

users = fetch_all_users(query="SELECT * FROM users")
print(f"query results: {users}")