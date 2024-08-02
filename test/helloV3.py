def main():
    name = input ("What's your name? ")
    output = title_case(name)
    print(hello(output))

def hello(to="world"):
    return f"hello, {to}"

def title_case(case="World"):
    case = case.title()
    return case

if __name__ == "__main__":
    main()
