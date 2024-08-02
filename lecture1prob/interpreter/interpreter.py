#Create a function to calculate user input's arithmetic
def main ():
    expression = input ("Arithmetic expression: ").strip ()
#not sure what to do when user input expression without spacing e.g. 1+1
    x,y,z = expression.split ()
    x = float (x)
    z = float (z)
#Condition where denominator cannot be 0
    if z == 0 and y == "/":
        print ("Denominator cannot be zero in division.")
        return
    result = float (calculator (x,y,z))
    print (f"{result:.1f}")

#Calculator for 4 different operations
def calculator (a,b,c):
    if b == "+":
        return a + c
    elif b == "-":
        return a - c
    elif b == "*":
        return a * c
    elif b == "/":
        return a / c

main ()
