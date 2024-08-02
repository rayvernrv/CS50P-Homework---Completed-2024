import inflect
p = inflect.engine()
name_list = []

while True:
    try:
        # split -> to split each word (user input) instead of each character
        name = input("Name: ").split()
        name_list += name
    except EOFError:
        print()
        break

print(f"Adieu, adieu, to {p.join(name_list)}")
