import sqlite3

# Connect to SQLite (or create a database)
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# Create table if not exists
cursor.execute('''
CREATE TABLE IF NOT EXISTS STUDENT (
    Name TEXT,
    Course TEXT,
    Grade TEXT,
    Score INTEGER
)
''')

# Insert 100 records
students_data = [
    ('Krish', 'Data Science', 'A', 90),
    ('Amit', 'Data Engineering', 'B', 85),
    ('Sneha', 'Machine Learning', 'A', 92),
    ('Rahul', 'Big Data', 'C', 78),
    ('Pooja', 'Artificial Intelligence', 'A', 95),
    ('Vikram', 'Data Science', 'B', 88),
    ('Neha', 'Data Engineering', 'A', 91),
    ('Rohit', 'Machine Learning', 'C', 75),
    ('Priya', 'Big Data', 'B', 82),
    ('Ankit', 'Artificial Intelligence', 'A', 96),
    ('Sonali', 'Data Science', 'B', 89),
    ('Arjun', 'Data Engineering', 'C', 77),
    ('Maya', 'Machine Learning', 'A', 94),
    ('Raj', 'Big Data', 'B', 81),
    ('Sita', 'Artificial Intelligence', 'A', 98),
    ('Aditya', 'Data Science', 'C', 76),
    ('Kavya', 'Data Engineering', 'B', 84),
    ('Suresh', 'Machine Learning', 'A', 93),
    ('Manoj', 'Big Data', 'C', 72),
    ('Divya', 'Artificial Intelligence', 'A', 97),
    ('Nitin', 'Data Science', 'B', 86),
    ('Swati', 'Data Engineering', 'A', 90),
    ('Tarun', 'Machine Learning', 'C', 74),
    ('Bhavya', 'Big Data', 'B', 83),
    ('Deepak', 'Artificial Intelligence', 'A', 95),
    ('Kiran', 'Data Science', 'C', 79),
    ('Varun', 'Data Engineering', 'B', 87),
    ('Meera', 'Machine Learning', 'A', 91),
    ('Yash', 'Big Data', 'C', 73),
    ('Rekha', 'Artificial Intelligence', 'A', 99),
]  

# Generate additional 70 random records
import random
names = ['Raj', 'Simran', 'Aman', 'Neha', 'Pankaj', 'Rita', 'Sohan', 'Ravi', 'Nisha', 'Kabir']
courses = ['Data Science', 'Data Engineering', 'Machine Learning', 'Big Data', 'Artificial Intelligence']
grades = ['A', 'B', 'C']
for _ in range(70):
    students_data.append((
        random.choice(names),
        random.choice(courses),
        random.choice(grades),
        random.randint(70, 100)
    ))

# Execute insert queries
cursor.executemany('''INSERT INTO STUDENT (Name, Course, Grade, Score) VALUES (?, ?, ?, ?)''', students_data)

# Commit and close
conn.commit()
conn.close()

print("100 records inserted successfully!")
