from seed import connect_to_prodev

def stream_users_in_batches(batch_size=2):

    offset= 0
    connection = connect_to_prodev()
    cursor = connection.cursor(dictionary=True)

    while True:
       cursor.execute("SELECT * FROM user_data LIMIT %s OFFSET %s",
                   (batch_size,offset))

       rows = cursor.fetchall()

       if not rows:
           break
       yield rows
       offset+=batch_size
       
    cursor.close()
    connection.close()

for batch in stream_users_in_batches():
    print(batch)




def batch_processing(batch_size =2):

    offset = 0
    connection = connect_to_prodev()
    cursor = connection.cursor(dictionary=True)

    while True:
       cursor.execute("SELECT * FROM user_data WHERE age > 25 LIMIT %s OFFSET %s ",
                      (batch_size,offset))
       rows = cursor.fetchall()

       if not rows:
           break
       yield rows
       offset+=batch_size

    cursor.closse()
    connection.close()
       


   

    