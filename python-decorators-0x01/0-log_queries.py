import sqlite3
from functools import wraps
from datetime import datetime



def log_queries(func):
    @wraps(func)
    def wrapper(*args,**kwargs):

        query = args[0] if args  else kwargs.get('query','no query provieded')
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"[{timestamp}] Executing query: {query}")
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