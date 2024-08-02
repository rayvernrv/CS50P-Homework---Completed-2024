# string method - split does not support regex

import re

name = input("Name: ").strip()

if matches := re.search(r"^(.+), *(.+)$", name): # (.+) capture group # walrus operator - return Boolean and assign right to left
    # last, first = matches.groups()
    # name = f"{first} {last}"
    name = matches.group(2) + " " + matches.group(1)
    print (f"hello, {name}")

elif matches := re.search(r"^\s*,*\s*$", name):
    print ("Wrong")

else:
    print(f"hello, {name}")

#how to reject when user input nothing or just space,space more effectively than above?
