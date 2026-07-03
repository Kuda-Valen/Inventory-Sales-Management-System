import os
import sqlite3


conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Enable foreign keys explicitly in SQLite
cursor.execute("PRAGMA foreign_keys = ON;")

# Base Table for all people (Managers, Cashiers, Customers)
cursor.execute("""
CREATE TABLE IF NOT EXISTS persons (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL, 
    last_name TEXT NOT NULL, 
    phone TEXT,
    email TEXT UNIQUE NOT NULL
);
""")

# Extension table specifically for Employees
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    person_id INTEGER PRIMARY KEY,
    role TEXT CHECK(role IN('Manager', 'Cashier')) NOT NULL,
    salary REAL NOT NULL,
    hire_date TEXT NOT NULL, -- Format: YYYY-MM-DD 
    username TEXT UNIQUE NOT NULL,
    hashed_password TEXT NOT NULL,
    FOREIGN KEY (person_id) REFERENCES persons(id) ON DELETE CASCADE
);
""")

conn.commit()
conn.close()

print("\nTables have been created successfully!")