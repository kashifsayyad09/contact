# db.py

import mysql.connector

# Connect to MySQL Server
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""  # add your password if needed
)

cursor = db.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS contactbook")

# Reconnect to the created database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="contactbook"
)

cursor = db.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS contacts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    phone VARCHAR(20),
    email VARCHAR(255)
)
""")

print("✅ Database and table created successfully.")
