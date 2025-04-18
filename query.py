import sqlite3

conn = sqlite3.connect('students.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM STUDENT")
records = cursor.fetchall()


# cursor.execute("SELECT Name, Score FROM STUDENT WHERE Score = (SELECT MAX(Score) FROM STUDENT)")
# records = cursor.fetchall()

for record in records:
    print(record)

conn.close()
