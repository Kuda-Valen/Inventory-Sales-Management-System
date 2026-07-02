from employee import Employee

class Cashier(Employee):
    def __init__(self, employee_id, salary, hire_date, username, password):
        super().__init__(employee_id, salary, hire_date, username, password)
    
    def create_oder(self):
        print("Create Order feature coming soon!")

    def accept_paymeht(self):
        print("Accept Payment feature coming soon!")
