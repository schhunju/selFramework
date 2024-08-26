import sqlite3

# Creating connection to the db
conn = sqlite3.connect('selDatabase.db')
cursor = conn.cursor()

# Creating  table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        address TEXT
    )
''')

# Inserting in table
cursor.execute("INSERT INTO users (name, age, address) VALUES (?, ?, ?)", ('Archana', 24, 'Kapan'))
cursor.execute("INSERT INTO users (name, age, address) VALUES (?, ?, ?)", ('Amrit', 45, 'Kapan'))

# Commit the insert operations
conn.commit()

# Reading data
print("Initial data:")
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Updating
cursor.execute("UPDATE users SET age = ? WHERE name = ?", (28, 'Amrit'))
conn.commit()

# Reading data after update
print("\nAfter update:")
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Deleting data
cursor.execute("DELETE FROM users WHERE name = ?", ('Amrit',))
conn.commit()

# Reading data after deleting
print("\nAfter deletion:")
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()
