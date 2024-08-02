i = 0
while i < 3: #Count from 0,1,2 - never through 3
    print ("meow")
    i += 1 #this is the same as  i = i + 1

print ("----------------------------------")

for i in [0,1,2]:
    print ("meow")

print ("----------------------------------")

for _ in range (4): #Can use "_" to represent i, as i is never use explicitly
    print ("meow")

print ("----------------------------------")
print ("meow\n"*3, end = "") #end "" is to prevent a new line

print ("----------------------------------")
#Prompt user for input until a correct value is keyed in, using while True:
while True:
    n = int (input ("What's n? "))
    if n > 0:
        break

for _ in range (n):
    print ("meow")
