import sys
import csv

from tabulate import tabulate

pizzas = []

try:
    if len(sys.argv) == 2:
        if sys.argv[1].endswith(".csv"):
            with open(sys.argv[1]) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    pizzas.append(row)
                print(tabulate(pizzas, headers="keys", tablefmt="grid"))
        else:
            sys.exit("Not a CSV file")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        raise FileNotFoundError

except FileNotFoundError:
    sys.exit("File does not exist")
