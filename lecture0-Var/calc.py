#Define the main function
def main ():
    a=int (input("What's a? "))
    print ("a squared is",square(a))

#Define what to do with argument by using the "return" function
def square (n):
    return pow (n,2)

main ()

#Define and learn about round of integers
x = float (input("What's x? "))
y = float (input("What's y? "))

z= round (x/y,2)
z1= round (x+y)

print (z)
print (f"{z1:,}") #comma is for to break 1000 into 1,000
