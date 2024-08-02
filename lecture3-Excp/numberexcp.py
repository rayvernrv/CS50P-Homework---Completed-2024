while True:
    try:
        x = int (input ("What's x? "))
    except ValueError:
        print ("Please input an integer.")
    else:
        break
print (f"x is {x}")

print ("-----------------------------------------------")

def main ():
    y = get_int("What's y?")
    print (f"y is {y}")

def get_int(prompt):
    while True:
        try:
            return int (input (prompt)) #this is the same as returning value y of user input and break out of while loop.
            #return is stronger than break
        except ValueError:
            print ("Please input an integer.") #or "pass" to stop repeating this statement

main()
