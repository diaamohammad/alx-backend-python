from seed import connect_to_prodev

def paginate_users(page_size,offset):

    connection = connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset} ")
    rows = cursor.fetchall()
    connection.close()
    cursor.close()
    return rows

def lazy_paginate(page_size):
    offset = 0
    while True:
      rows = paginate_users(page_size,offset)
    
      if not rows:
        break
      yield rows
      offset+=page_size
for row in lazy_paginate(1):
   
   print(row)


    

