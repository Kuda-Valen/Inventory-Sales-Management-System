
class Payment():
    def __init__(self, payment_id, amount, method, date):
        self.payment_id = payment_id
        self.amount = amount
        self.method = method
        self.date = date
    
    def process(self):
        print("Process Payment feature coming soon!")
    
    def refund(self):
        print("Refund feature coming soon!")