#Print snake case when user input in camel case
def main ():
    camel_1=input ("camelCase: ")
    snake_1 = camel_to_snake (camel_1)
    print ("snake case: ",snake_1)

#Define a function to change camel_case (c) to snake_case (s)
#by looping into each character in user input
def camel_to_snake (camel):
    snake = ""
    for char in camel:
        if char.islower():
            snake += char.lower()
        elif char.isupper():
            snake += "_" + char.lower()
        else:
            snake += char
    return snake

main ()
