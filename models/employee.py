from person import Person

class Employee(Person):
    def __init__(self, id, first_name, last_name, phone, email, employee_id, salary, hire_date, username, password):
        super().__init__(id, first_name, last_name, phone, email)
        self.employee_id = employee_id
        self.salary = salary
        self.hire_date = hire_date
        self.username = username
        self.password = password

    def login(self):
        print("Login feature coming soon!")

    def logout(self):
        print("Logout feature coming soon!")