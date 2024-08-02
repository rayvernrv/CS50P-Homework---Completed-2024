import csv

class Item:
    pay_rate = 0.8 # class attribute
    all = []
    def __init__(self, name: str, price: float, quantity=0): #default value if unsure the value, # float can be int # = 0 is already integer
        # Run validation to the received arguments
        assert price >= 0, f"Price {price} cannot be less than 0"
        assert quantity >= 0, f"Quantity {quantity} cannot be less than 0"

        # Assign to self object
        self.__name = name
        self.price = price
        self.quantity = quantity

        # Action to execute
        Item.all.append(self)

    @property # getter -> read only, disallow user to change
    def name(self):
        return self.__name

    @name.setter # for a certain condition
    def name(self, value): # must receive 1 parameter
        if len(value) > 10:
            raise Exception("The name is too long")
        else:
            self.__name = value

    def calculate_total_price(self): # self passes the instance itself as 1st argument
        return self.price * self.quantity # attributes assigned in __init__ when instantiated, so we can access

    def apply_discount(self):
        self.price = self.price * self.pay_rate # must be self.payrate -> to account for different pay_rate of different instances

    @classmethod # class method -> Item.instantiate_from_csv
    def instantiate_from_csv(cls): # this is to create the object or (self), cannot be need to be class method. cls is class reference as first arg
        with open("items.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name = item.get("name"), # name here on LHS is the name in self.name = name RHS, to assign name to name for instantiation of object
                price = float(item.get("price")),
                quantity = float(item.get("quantity")),
            )

    @staticmethod # static method -> only
    def is_int(num):
        # Exclude floats that are point zero i.e 100.0
        # Usually calling this by Item.is_int() at class level, rarely at instance level
        if isinstance(num, float): # built in function
            return num.is_integer() # is_integer is a method to exclude point zero as float, then return True
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})" # Python best practice to represent the instance




""" Class methods
Item.instantiate_from_csv()
print(Item.all)
"""

item1 = Item("Phone", 100, 2) # calls __init__ to instantiate
# item2 = Item("Laptop", 1000, 3)
# item3 = Item("Cable", 10, 5)
# item4 = Item("Mouse", 50, 5)
# item5 = Item("Kayboard", 75, 5)

print(item1.calculate_total_price())


# for instance in Item.all:
#     print(instance.name)

# print(item1.name)
# print(item2.name)
# item2.pay_rate = 0.7 # override 0.8
# item2.apply_discount()
# print(item2.price)


# item2.has_numpad = False # can still assign attribute to specific instances individually
# print(item1.pay_rate) #find at instance level, cannot find, will find it in class level
# print(Item.__dict__) to see the attribute in class or, item.__dict__ to see the attribute in instance
