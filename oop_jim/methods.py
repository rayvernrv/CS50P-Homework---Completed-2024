# Class Method vs Static Method

class Item:
    @staticmethod
    def is_int(num):
        # Relationship with the class, but not unique per instance
        # pass variable as first argument
        # Usually calling this by Item.is_int() at class level, rarely at instance level

    @classmethod
    def instantiate_from_csv(cls):
        # Relationship with the class, but used to manipulate different data structure to instantiate object
        # pass class as first argument (mandatory parameter)
