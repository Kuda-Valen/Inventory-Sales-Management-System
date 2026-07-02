
class Order():
    def __init__(self, order_id, customer, employee, date, status, items, total):
        self.order_id = order_id 
        self.customer = customer 
        self.employee = employee
        self.date = date
        self.status = status
        self.items = items
        self.total = total

    def calculate_total(self):
        print("Calculate total feature coming soon!")

    def print_receipt(self):
        print("Print receipt feature coming soon!")

    def cancel(self):
        print("Cancelling Order feature coming soon!")