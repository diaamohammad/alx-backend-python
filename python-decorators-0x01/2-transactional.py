
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




def transactional(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        conn = args[0]
        try:
            result = func(*args,**kwargs)
            conn.commit()
            return result

        except Exception as e:
            conn.rollback()
            raise
    return wrapper


@with_db_connection
@transactional
def update_user_email(conn, user_id, new_email):
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET email=?WHERE id =?",(new_email,user_id))
    

if __name__ == "__main__":
    try:
        update_user_email(user_id=1, new_email='diaa@example.com')
        # اختبار التحديث
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (1,))
        print(cursor.fetchone())
        conn.close()
    except Exception as e:
        print(f"Error: {e}")


        