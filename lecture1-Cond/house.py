name = input ("What's your name? ")

#Option 1 using if/elif/else
if name == "Harry" or name == "Hermione":
    print ("Gryffindor")
elif name == "Draco":
    print ("Slytherin")
else:
    print ("Who?")

#Option 2 using match
match name:
    case "Harry" | "Hermione" | "Ron":
        print ("Gryffindor")
    case "Draco":
        print ("Slytherin")
    case _:
        print ("Who?")
