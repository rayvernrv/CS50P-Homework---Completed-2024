#To take in any user input
def main ():
    with_vowel = input ("Input: ").strip()
    no_vowel = elim (with_vowel) #use elim function to omit vowels
    print ("Output:", no_vowel)

def elim (user_input):
    vowel = ["a","e","i","o","u","A","E","I","O","U"]
    new_output = ""
    for char in user_input:
        if char in vowel: #if vowel is found while looping user_input, continue without printing vowel
            continue
        else:
            new_output += char
    return new_output

main()

"""
My own reference about not in
for char in user_input:
    if char not in vowel:
        new_output += char
    else:
        None #not needed
return new_output
"""
