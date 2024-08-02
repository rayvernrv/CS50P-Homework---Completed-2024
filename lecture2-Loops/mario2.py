def main ():

    print_square (3)

def print_square (size):
    #For each row in square
    for row in range (size):
        #For each brick in row = column
        for column in range (size):
            #Print brick
            print ("#",end="")
        print ()
    #Simpler version in 2nd part of mario.py
main ()
