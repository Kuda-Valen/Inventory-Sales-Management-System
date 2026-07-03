import sqlite3
import hashlib
from models.employee import Employee


def find_employee(username: str) -> Employee | None:
               
    conn = sqlite3.connect("database/database.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    try:
        query = """
            SELECT p.first_name, p.last_name, p.phone, p.email, e.role, e.salary, e.hire_date, e.username, e.hashed_password
            FROM employees e
            INNER JOIN persons p ON person_id = p.id
            WHERE e.username = ?;
            """
        cursor.execute(query, (username.strip(),))
        row = cursor.fetchone()

        if row is None:
            return None

        return Employee(
            first_name=row["first_name"],
            last_name=row["last_name"],
            phone=row["phone"],
            email=row["email"],
            role=row["role"],
            salary=row["salary"],
            hire_date=row["hire_date"],
            username=row["hire_date"],
            hashed_password=row["hashed_password"]
            )    

    except sqlite3.Error as e:
        print(f"Search failed: {e}")
        return None
    
    finally:
        conn.close()
    
def authenticate() -> Employee | None:
    print("\n-- System Login --\n")
    username = input("Enter Username: ").strip()
    employee = find_employee(username)

    if employee is None:
        print("\nAuthentication Failed: User does not exist.")
        return None
    
    password = input("Enter Password: ").strip()
    input_hash = hashlib.sha256(password.encode()).hexdigest()

    if input_hash == employee.hashed_password:
        print(f"\nWelcome back, {employee.first_name}! Logged in as '{employee.role}'")
        return employee
    else:
        print("\nAuthentication Failed: Invalid Password.")
        return None

    

