students = ["Bubu", "Yier", "Labong", "Avoca"] #List []

#the [list] is in 0,1,2. Below will print students in [1]
print (students [1])

print ("-----------------------------------")

#Iterate students which is in the list, and print out 1 by 1
for name in students:  #or for name in ["Bubu", "Yier", "Labong"] list
    print (name)

print ("-----------------------------------")
for i in range (len(students)): #len is short for length, it will count the number of items in list
    print (i+1, students [i])

print ("-----------------------------------")
#Dictionary {}
players = {
    "Bubu" :"Brown",
    "Yier" : "White",
    "Labong" : "Orange",
    "Avoca" : "Green",
}

for name in players:
#print (name) will by design show keys only from player dict, which is Bubu, Yier...
#so, (name) is made up, and refer to the key, which is Bubu, Yier
    print (name, players [name], sep="-")
