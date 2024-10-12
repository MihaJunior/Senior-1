import sqlite3

conn = sqlite3.connect('temperature.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS weather_data (
                time TEXT,
                temperature TEXT
            )''')

c.execute("INSERT INTO weather_data (time, temperature) VALUES ('2024-10-12 19:49', 22.5)")
c.execute("INSERT INTO weather_data (time, temperature) VALUES ('2024-10-12 20:00', 21.8)")

conn.commit()
conn.close()
