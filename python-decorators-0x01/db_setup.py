import sqlite3

conn = sqlite3.connect('users.db')
cursor  = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  email TEXT UNIQUE                        
)
''')

cursor.execute("INSERT OR IGNORE INTO users (name, email) VALUES ('Diaa', 'ahmed@example.com')")
cursor.execute("INSERT OR IGNORE INTO users (name, email) VALUES ('Mohammed', 'mohammed@example.com')")
cursor.execute("INSERT OR IGNORE INTO users (name, email) VALUES ('Amira', 'sara@example.com')")

conn.commit()
conn.close()

print("Database 'users.db' created successfully with 'users' table and sample data!")