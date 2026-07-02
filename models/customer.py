from person import Person

class customer(Person):
    def __init__(self, id, first_name, last_name, phone, email, customer_id, loyalty_points, purchase_history):
        super().__init__(id, first_name, last_name, phone, email)
        self.customer_id = customer_id
        self.loyalty_points = loyalty_points
        self.purchase_history = purchase_history

    def buy_product(self):
        print("this feature is coming soon!")
    
    def view_orders(self):
        print("This feature is coming soon!")
