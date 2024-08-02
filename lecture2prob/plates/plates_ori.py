def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if 2 <= len (s) <= 6: #check statement is between 2 and 6 characters
        if s.isalpha(): #if alphabet, means valid, no need to check for numbers
            return True
        elif s.isalnum() and s[0:2].isalpha(): #if mix of alphabet and numbers, and 1st 2 characters are alphabet
            for char in s: #to iterate each character in s
                if char.isdigit(): #in each iteration, found character is a digit
                    #for char iteration stop when found digit, is about finding digit
                    location = s.index(char) #locate the nth character of the statement and assign as location (integer) --> using index function
                    if s[location:].isdigit() and s[location] != "0": #s[location:] --> is a slicing method to know the character after location (int) isdigit or not
                        return True
                    else:
                        return False

main ()
