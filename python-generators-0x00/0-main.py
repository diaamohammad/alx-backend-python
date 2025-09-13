seed = __import__('seed')

connection = seed.connect_db()

if connection:

    seed.create_database(connection)
    connection.close()
    print('connection succfull')

connection = seed.connect_to_prodev()
if connection:
    seed.create_table(connection)
    print('table is done ') 
    seed.insert_data(connection, 'user_data.csv')
    print('done') 

    for row in seed.streem_rows(connection):
   
        print(row)

