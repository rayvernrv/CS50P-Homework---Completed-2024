import csv

students = []

with open("before.csv") as bef_file:
    reader = csv.DictReader(bef_file)
    for row in reader:
        last, first = row["name"].split(", ")
        students.append({"first": first, "last": last, "house": row["house"]})

for student in students:
    print (student)
