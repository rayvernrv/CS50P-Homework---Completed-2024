import sys

try:
    if len(sys.argv) == 2:
        if sys.argv[1].endswith(".py"):
            with open(sys.argv[1]) as file:
                i = 0
                for row in file:
                    if row.lstrip().startswith("#") or row.startswith("#") or row.isspace():
                        i += 0
                    else:
                        i += 1
                print (i)
        else:
            sys.exit("Not a Python file")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        raise FileNotFoundError

except FileNotFoundError:
    sys.exit("File does not exist")
