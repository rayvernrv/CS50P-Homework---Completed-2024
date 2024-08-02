items = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }

total = 0
while True:
    try:
        item = input ("Item: ").title().strip()
        price = items[item] #instead of if item in items, this can be catched by raising KeyError when wrongly input
        total += price
        print (f"Total: ${total:.2f}")
    except EOFError:
        print ()
        break
    except KeyError:
        pass
