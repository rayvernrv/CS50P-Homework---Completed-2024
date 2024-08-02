#Determine if a number is even or odd

def main (n=None):
#None is a built in constant to reresent the absence of a value
#If no argument when main is called, it will default to None
#Else it will take in new value for n
    if n is None:
        x = int (input ("What's x? "))
    else:
        x = n
    if is_even (x):
        print ("Even")
    else:
        print ("Odd")

def is_even (a):
    if a % 2 == 0:
        return True
    else:
        return False

main ()

#Testing to use main function below with new argument
y = int (input("What's y? "))
main (y)

b = int (input("What's b? "))
main (b)
