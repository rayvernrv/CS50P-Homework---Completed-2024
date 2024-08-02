def main ():
    brick = int (input ("number of brick: "))
    build (brick)
    print ("----------------------------")
    print_square (brick)

def build (height):
    for _ in range (height):
        print ("#")

def print_square (size):
    #print each row in square
    for _ in range (size):
        print ("#" * size) #in each loop, it will print # in each row,
                           #then print will end in next line

"""print ("#\n" * height, end="")
#just showing another way of printing
#but this will result in 'height' times x 'height'
"""

main ()
