#To take in any user input
def main ():
    with_vowel = input ("Input: ").strip()
    no_vowel = shorten (with_vowel) #use shorten function to omit vowels
    print ("Output:", no_vowel)

def shorten (word):
    vowel = ["a","e","i","o","u","A","E","I","O","U"]
    new_output = ""
    for char in word:
        if char in vowel: #if vowel is found while looping user_input, continue without printing vowel
            continue
        else:
            new_output += char
    return new_output

if __name__ == "__main__":
    main ()

