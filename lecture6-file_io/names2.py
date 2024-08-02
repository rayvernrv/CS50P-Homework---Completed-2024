names = []

with open("names.txt") as name_file:
    for line in name_file:
        names.append(line.rstrip()) #append to the list, not appending to the file

print (sorted(names)) #it's a list

for name in sorted(names):
    print(f"hello, {name}")

print("------------------------------")
#This way is shorter form if we want to sort immediately. but not friendly to work on the data more before printing
with open("names.txt") as name_file:
    for line in sorted(name_file):
        print(f"hello, {line}".rstrip())

print("------------------------------")

with open("names.txt") as name_file:
    for line in sorted(name_file,reverse=True):
        print(f"hello, {line}".rstrip())
