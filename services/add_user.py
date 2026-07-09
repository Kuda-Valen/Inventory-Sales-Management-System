import hashlib
import sqlite3
from models.employee import Employee
from models.customer import Customer
from datetime import datetime


def add_user():
    print("\n--Add New User --\n")
    print("1. Add Employee")
    print("2. Add Customer")
    print("3. Return to Main Menu")
    
    try:
        option = int(input("\nChoose an Option: "))

        if option == 1:
            print("\n-- Add New Employee -- \n")
            first_name = input("Enter First Name: ").strip()
            last_name = input("Enter Last Name: ").strip()
            phone = str(input("Enter Phone Number: ")).strip()
            email = str(input("Enter Email Address: ")).strip()
            role = input("Enter Empoyee Role ['Manager', 'Cashier']: ").strip()
            while role not in ["Manager", "Cashier"]:
                role = input("Invalid role! Enter exactly 'Manager' or 'Cashier': ").strip()

            salary = input("Enter Salary: R").strip()
            hire_date = input("Enter Hire Date in the format [YYYY-MM-DD]: ").strip()

            while not validate_date(hire_date):
                hire_date = input("Invalid format! Enter Hire Date using [YYYY-MM-DD]: ").strip()

            username = input("Enter Employee Username: ").strip()
            password = str(input("Enter password: "))
            hashed_password = hash_password(password)

            employee = Employee(first_name, last_name, phone, email, role, salary, hire_date, username, hashed_password)

            save_employee_to_sql(employee)
    
        elif option == 2:
            print("\n -- Add Customer --\n")
            first_name = str(input("Enter Customer Name: ")).strip()
            last_name = str(input("Enter Customer Last Name: ")).strip()
            phone = str(input("Enter Customer Phone number: ")).strip()
            email = str(input("Enter Customer Email: ")).strip()

            customer = Customer(first_name, last_name, phone, email)

            save_customer_to_sql(customer)

        elif option == 3:
            print("Returning to Main Menu")
            return
        else:
            print("Invalid option! Select a Valid Option.")

    except ValueError as e:
        print(f"\nInvalid input! An error occured: {e}")

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def validate_date(date_str: str) -> bool:
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def save_employee_to_sql(employee: Employee):
    conn = sqlite3.connect("database/database.db")
    cursor = conn.cursor()

    try:
        cursor.execute("PRAGMA foreign_keys = ON;")

        with conn:
            cursor.execute(
            """
            INSERT INTO persons (first_name, last_name, phone, email) VALUES (?, ?, ?, ?);
            """,
            (employee.first_name, employee.last_name, employee.phone, employee.email)
            )
        
            generated_person_id = cursor.lastrowid

            cursor.execute(
                """
                INSERT INTO employees (person_id, role, salary, hire_date, username, hashed_password) 
                VALUES (?, ?, ?, ?, ?, ?);
                """,
                (
                    generated_person_id, 
                    employee.role, 
                    float(employee.salary),
                    employee.hire_date,
                    employee.username, 
                    employee.hashed_password
                )
            )

        print(f"\nEmployee '{employee.first_name}' successfully aded with System ID: {generated_person_id}")
    
    except sqlite3.IntegrityError as e:
        print(f"\nDatabase error: The email or username already exists! ({e})")
    
    except Exception as e:
        print(f"\nAn unexpected database storage error occured: {e}")

    finally:
        conn.close()

def save_customer_to_sql(customer: Customer):
    conn = sqlite3.connect("database/database.db")
    cursor = conn.cursor()

    try:
        cursor.execute("PRAGMA foreign_keys = ON;")

        with conn:
            cursor.execute(
                """
                INSERT INTO persons (first_name, last_name, phone, email) VALUES (?, ?, ?, ?);
                """,
                (customer.first_name, customer.last_name, customer.phone, customer.email)
            )

            generated_person_id = cursor.lastrowid

            cursor.execute(
                """
                INSERT INTO customers (person_id, loyalty_points) VALUES (?, ?);
            """,
            (generated_person_id, getattr(customer, 'loyalty_points', 0));
            )
            
        print(f"Customer '{customer.first_name}' successfully added with System ID: {generated_person_id}")
    
    except sqlite3.IntegrityError as e:
        print(f"\nDatabase error: Email already exists! ({e})")
    
    except Exception as e:
        print(f"\nAn unexpected database storage error occured: {e}")
    
    finally:
        conn.close()