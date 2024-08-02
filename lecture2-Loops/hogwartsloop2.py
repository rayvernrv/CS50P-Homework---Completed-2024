students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Dog"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for student in students: #for each key
    print (student ["name"], student ["house"], student ["patronus"], sep = ", ") #find value for each key
