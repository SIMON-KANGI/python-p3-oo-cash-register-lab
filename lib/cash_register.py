class CashRegister:
    def __init__(self, discount=0):
        self._discount = discount
        self.items = []  
        self._total = 0

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, discount):
        self._discount = discount

    @property
    def total(self):
        return self._total

    def add_item(self, title, price):
        self.items.append((title, price))  
        self._total += price
        print("total updated successfully")

    def void_last_transaction(self):
        if self.items:  
            title, price = self.items.pop() 
            self._total -= price 
            
    def apply_discount(self):
        return (self.total *self.discount) /100

register = CashRegister(discount=10) 

register.add_item("Apple", 2.5)
register.add_item("Banana", 1.5)
register.add_item("Orange", 3.0)

print("Total before discount:", register.total)


discounted_total = register.total * (1 - register.discount / 100)
print("Total after discount:", discounted_total)


register.void_last_transaction()
print("Total after voiding last transaction:", register.total)
print(register.items)
