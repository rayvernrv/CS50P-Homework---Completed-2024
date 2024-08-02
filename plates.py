def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if 2 <= len (s) <= 6:
        if s.isalpha():
            return True
        elif s.isalnum() and s[0:2].isalpha():
            for char in s:
                if char.isdigit():
                    location = s.index(char)
                    if s[location:].isdigit() and s[location] != "0":
                        return True
                    else:
                        return False
        else:
            return False
    else:
        return False

if __name__ == "__main__":
    main()
