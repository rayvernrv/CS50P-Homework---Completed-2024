#csv #dictreader
import csv

students = []

with open("students2.csv") as file:
    reader = csv.reader(file) #returns a list
    for name,home in reader:
        students.append({"name": name, "home": home})

for student in sorted(students, key=lambda stdn: stdn["home"]): #key=lambda is equivalent to def get_name. stdn is coder specify
    print (f"{student['name']} is from {student['home']}")

print ("-----------------------------------------------------")

students = []

with open("students2.csv") as file:
    reader = csv.DictReader(file) #returns a dict, #first row of csv must be header
    for row in reader:
        students.append({"name": row["name"], "home": row["home1"]}) #home1 must be the same as 1st row title
        #students.append(row) - alternatively

for student in sorted(students, key=lambda stdn: stdn["home"]): #key=lambda is equivalent to def get_name. stdn is coder specify
    print (f"{student['name']} is from {student['home']}")
    #"home" must be the same as row 20,22,23
    #if using row 21, then row 23,24 ["xxxx"] where xxxx must be the same as title
