def main():
    hello ("world")
    goodbye ("world")

def hello (name):
    print (f"hello, {name}")

def goodbye (name):
    print (f"goodbye, {name}")

#main() -> wrong if other file wanna use the function

if __name__ == "__main__":
    main()
