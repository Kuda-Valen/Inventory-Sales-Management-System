import os 
import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("PRAGMA foreign_keys = ON;")

# Tables for Products
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL, 
    cost_price REAL NOT NULL, 
    selling_price REAL NOT NULL,
    stock INTEGER NOT NULL,
    supplier_name TEXT NOT NULL
);
""")

conn.commit()
conn.close()

print("\nProducts Table has been created successfully...")