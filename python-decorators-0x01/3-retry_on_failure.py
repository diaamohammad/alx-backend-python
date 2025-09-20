import sqlite3
from functools import wraps
import time


def with_db_connection(func):
    @wraps(func)
    def wrapper(*args,**kwargs):

        conn = sqlite3.connect('users.db')
        result = func(conn, *args, **kwargs)
        conn.close()
        return result
    return wrapper


def retry_on_failure(retires=3,delay=2):

    def decorator(func):
        
        @wraps(func)
        def wrapper(*args,**kwargs):
            attempt=1
            last_excption = None
            while attempt <= retires:
                try:
                    return func(*args,**kwargs)
                except (sqlite3.OperationalError, sqlite3.DatabaseError) as e:
                    
                    last_excption = e
                    if attempt == retires:
                        raise last_excption
                    time.sleep(delay)
                    attempt =+1
            raise last_excption
        return wrapper
    return decorator


@with_db_connection
@retry_on_failure()
def fetch_users_with_retry(conn):
    cursor= conn.cursor()
    cursor.execute('SELECT * FROM users')
    return cursor.fetchall()


users=fetch_users_with_retry()
print(users)
    


       

        
 