from models.person import Person

class Customer(Person):
    def __init__(self, first_name, last_name, phone, email):
        super().__init__( first_name, last_name, phone, email)
        self.loyalty_points = 0
        self.purchase_history = None

    def buy_product(self):
        print("this feature is coming soon!")
    
    def view_orders(self):
        print("This feature is coming soon!")
