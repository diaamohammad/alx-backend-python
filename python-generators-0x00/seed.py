import os
from dotenv import load_dotenv
load_dotenv()
import csv
import mysql.connector


def connect_db():

    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST","localhost"),
            user=os.getenv("DB_USER","root"),
            password=os.getenv("DB_PASS","")
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None


  
def create_database(connection):
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
    cursor.close()




def connect_to_prodev():
    try:

        connection = mysql.connector.connect(
           host = os.getenv("DB_HOST","localhost"),
           user = os.getenv("DB_USER","root"),
           password = os.getenv("DB_PASS",""),
           database=os.getenv("DB_NAME", "ALX_prodev")
        )
        return connection

    except mysql.connector.Error as err:
        print(f"Error:{err}")
        return None
      
     


def create_table( connection):
    cursor = connection.cursor()
    cursor.execute (""" 
       CREATE TABLE IF NOT EXISTS USER_DATA(
           user_id CHAR(36) PRIMARY KEY,
           name VARCHAR(255) NOT NULL,
           email VARCHAR(255) NOT NULL,
           age DECIMAL NOT NULL,
           INDEX(user_id)
                      
        )
    """)
    cursor.close()
    




def insert_data(connection,csv_file):
    cursor = connection.cursor()
    with open(csv_file,newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            cursor.execute("""
                  INSERT IGNORE INTO user_data (user_id,name,email,age)
                  VALUES (%s,%s,%s,%s)
            """, (row['user_id'], row['name'], row['email'], row['age']))
    connection.commit()
    cursor.close()

        


def streem_rows(connection):
    cursor = connection.cursor()
    cursor.execute(" SELECT * FROM user_data")

    for row in cursor:
        yield row
    cursor.close()