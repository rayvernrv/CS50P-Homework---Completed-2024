#Using indexing row[0]
with open("students.csv") as students_file:
    for line in students_file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is {row[1]} color")

print ("-------------------------------------------")
#Using 2 variables assigned
with open("students.csv") as students_file:
    for line in sorted(students_file): #only sort by the 1st column
        name,color = line.rstrip().split(",")
        print(f"{name} is {color} color")

print ("-------------------------------------------")
#Sort the student names - Version 1 (only 1st column)
students = []

with open("students.csv") as students_file:
    for line in students_file:
        name,color = line.rstrip().split(",")
        students.append(f"{name} is {color} color")

for student in sorted(students):
    print(student)

print ("-------------------------------------------")
#Sort again - Version 2, can sort by either keys and not just the 1st column
students = []

with open("students.csv") as students_file:
    for line in students_file:
        name,color = line.rstrip().split(",")
        student = {"name": name, "color": color}
        students.append(student)

def get_name(student): #in dictionary
    return student["name"] #dont have to be student[], can be any

def get_color(student): #in dictionary
    return student["color"]

for student in sorted(students,key=get_color, reverse=True): #not using key=get_name(), no (), means it allows sorted to call the get_name function
    print (f"{student['name']} is {student['color']} color")

print ("-------------------------------------------")
#lambda function - a function to replace function that only appears once, like for _ in range
for student in sorted(students, key=lambda lala: lala["color"]): #key=lambda is equivalent to def get_name. lala is coder specify, "color" must be the same unpact in row32
    print (f"{student['name']} is {student['color']} color")
