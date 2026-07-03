from models.person import Person

class Employee(Person):
    def __init__(self, first_name, last_name, phone, email, role, salary, hire_date, username, hashed_password):
        super().__init__( first_name, last_name, phone, email)
        self.role = role
        self.salary = salary
        self.hire_date = hire_date
        self.username = username
        self.hashed_password = hashed_password

    def login(self):
        print("Login feature coming soon!")

    def logout(self):
        print("Logout feature coming soon!")