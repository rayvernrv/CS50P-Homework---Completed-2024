from item import Item

# Inheritance -> to use the functionalities from Item class
class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phone=0): #default value if unsure the value, # float can be int # = 0 is already integer
        # Call super() to access all attributes/methods in Item class
        super().__init__(name, price, quantity)

        # Run validations
        assert broken_phone >= 0, f"Broken phone {broken_phone} cannot be less than 0"

        # Assign to self object
        self.broken_phone = broken_phone

"""
phone1 = Phone("Iphone", 500, 5)
Item.instantiate_from_csv()
print(Item.all) # better use parent class Item.all, to call the child class
"""

""" Inheritance
phone1 = Phone("Iphone", 500, 5)
print(phone1.calculate_total_price())
phone2 = Phone("Samsung", 500, 5)
"""
