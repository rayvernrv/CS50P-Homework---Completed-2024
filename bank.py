#If input "Hello", no penalty fees
#If input starts with "H", $20 penalty fees
#Otherwise, $100 penalty fees

def main():
    greetings = input("Greeting: ")
    paid = value(greetings)
    print(f"${paid}")

def value(greeting):
    greeting = greeting.lower().strip().replace (" ","")
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
