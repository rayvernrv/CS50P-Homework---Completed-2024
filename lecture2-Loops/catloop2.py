def main ():
    number = get_number ()
    meow (number)

def get_number ():
    while True:
        n = int (input ("What's n? "))
        if n > 0:
            return n #if "break" here, code won't run. need to return to hand back value n
    # or can break, then return n in the next line

def meow (n):
    for _ in range (n):
        print("meow")

main ()
