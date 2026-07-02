from employee import Employee

class Manager(Employee):
    def __init__(self, employee_id, salary, hire_date, username, password):
        super().__init__(employee_id, salary, hire_date, username, password)
    
    def add_product(self):
        print("Add product feature coming soon!")
    
    def remove_product(self):
        print("Remove product feature coming soon!")

    def generate_report(self):
        print("Reports feature coming soon!")

    def hire_employee(self):
        print("Hiring staff feature coming soon!")

    def create_order(self):
        print("Create Order feature coming soon!")

    def accept_payment(self):
        print("Accept payment feature coming soon!")