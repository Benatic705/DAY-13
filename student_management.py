import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="student_db"
)

cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    department VARCHAR(50)
)
""")

# Insert
cursor.execute(
    "INSERT INTO students VALUES (1,'John',20,'CSE')"
)

# Read
cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(row)

# Update
cursor.execute(
    "UPDATE students SET age=21 WHERE id=1"
)

# Delete
cursor.execute(
    "DELETE FROM students WHERE id=1"
)

conn.commit()
conn.close()
