#Ask user for their name, remove white space before/after/between string, capitalize 1st letter of each word
name = input ("What's your full name? ").title()

name =" ".join(name.split())

#Split user's name into first and last name
first,last = name.split(" ")


#Say hello to user
print (f"hello, {name}")




