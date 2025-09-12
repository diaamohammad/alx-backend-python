Python Generators – Database Seeder

This project sets up a MySQL database and seeds it with sample user data from a CSV file.

Requirements

Python 3.8+

MySQL Server 8+

mysql-connector-python package

Install dependencies:

pip install mysql-connector-python

Setup
1. Set MySQL password as environment variable

Before running, export your MySQL root password into an environment variable:

Windows (PowerShell):

$env:DB_PASS="YourPasswordHere"


Linux / Mac (bash/zsh):

export DB_PASS="YourPasswordHere"

2. Run the main script
python 0-main.py


Expected output:

connection successful
Table user_data created successfully
Database ALX_prodev is present
[('uuid1', 'Name1', 'email1', 25), ('uuid2', 'Name2', 'email2', 30), ...]

Files

seed.py → contains the functions for database setup and data insertion.

user_data.csv → sample data to be inserted into the database.

0-main.py → test file to verify your implementation.

README.md → setup and usage instructions.

Functions in seed.py

connect_db() → connects to MySQL server

create_database(connection) → creates ALX_prodev database if it does not exist

connect_to_prodev() → connects to ALX_prodev database

create_table(connection) → creates user_data table if it does not exist

insert_data(connection, data) → inserts CSV data into the table