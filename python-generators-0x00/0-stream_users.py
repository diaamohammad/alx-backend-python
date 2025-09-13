

def stream_users(connection):

    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data")
    for row in cursor:
        yield row

    cursor.close()




    def stream_users()

    

