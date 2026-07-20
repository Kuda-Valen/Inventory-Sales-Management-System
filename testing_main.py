import sqlite3
# lets see if it works...

"""Inventory & Sales Management System"""
print("Inventory & Sales Management System")

def admin_menu():
    print("\n1. Add Product")
    print("2. Remove Product")
    print("3. Edit Product")
    print("4. View Products")
    print("5. View Sales")
    print("6. Sales")

def staff_menu():
    print()

def customer_menu():
    print("\n1. Browse Products")
    print("2. Buy Product")
    print("3. Order History")
    print("4. Search Products")

def add_user():
    name = input("Enter name: ")
    surname = input("Enter last name: ")
    phone = str(input("Enter phone number: "))
    email = str(input("Enter email: "))

    conn = sqlite3.connect("Users.db")
    cursor = conn.cursor()

    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS users(
            name TEXT NOT NULL,
            surname TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT NOT NULL
        )
    """    
    )
    conn.commit()

    try:
        cursor.execute(
            "INSERT INTO users (name, surname, phone, email) VALUES (?, ?, ?, ?)",
            (name, surname, phone, email),
        )
        conn.commit()
        print(f"\nSuccessfully added '{name}' to the database!")
    except sqlite3.IntegrityError:
        print(f"Error: User with the email '{email}' already exist")

    finally:
        conn.close()

add_user()