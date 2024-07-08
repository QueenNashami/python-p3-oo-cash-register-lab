# lib/cash_register.py

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.transactions = []

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        for _ in range(quantity):
            self.items.append(title)
        self.transactions.append(price * quantity)

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.transactions:
            last_transaction = self.transactions.pop()
            self.total -= last_transaction