import sys
import csv

try:
    if len(sys.argv) == 3:
        if sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv"):
            students = []
            with open(sys.argv[1]) as bef_file:
                reader = csv.DictReader(bef_file)
                for row in reader:
                    # row["header_title"] can be split further into 2 var
                    last, first = row["name"].split(", ")
                    # then append to students list by assigning 3 of var
                    students.append({"first": first, "last": last, "house": row["house"]})
            with open(sys.argv[2], "w") as aft_file:
                writer = csv.DictWriter(aft_file, fieldnames=["first", "last", "house"])
                writer.writeheader()  # method to include writing of header
                writer.writerows(students)
        elif sys.argv[1].endswith(".csv") == False and sys.argv[2].endswith(".csv") == False:
            sys.exit("Not a csv file")
        else:
            raise FileNotFoundError

    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        raise FileNotFoundError

except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")
