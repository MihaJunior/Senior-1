import sqlite3
connection = sqlite3.connect('itstep_DB.sl3', 5)
cursor = connection.cursor()

cursor.execute('create table weather(name text, password text);')

connection.commit()

# print(connection)
# print(cursor)

connection.close()