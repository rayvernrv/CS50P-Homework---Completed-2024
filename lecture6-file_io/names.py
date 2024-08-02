#2 methods to read from a file
#but it's just for reading and printing at the same time, you can make-do with the data before printing
#refer names2.py for solution

with open("names.txt", "r") as name_file:
    lines = name_file.readlines()

for line in lines:
    print (f"hello, {line}".rstrip())

print ("----------------------------------------")

with open("names.txt") as name_file: #no need "r", it's actually the default
    for line in name_file:
        print (f"hello, {line}".rstrip())
