import re

email = input("Email: ").strip()

#if re.search(r"^[^@]+@[^@]+\.edu$", email): # r"" -> raw string, [^@] any character except "@" on the left and right of "@"
#if re.search(r"^[a-zA-Z0-9_ ]+@[a-zA-Z0-9_ ]+\.edu$", email): # can put a space to allow space in []
#if re.search(r"^\w+@\w+\.(edu|com|gov)$", email, re.IGNORECASE): # or (\w|\s) to allow space

if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE): # ? tell (\w+\.) can be 0 or 1, not there or there --> can replace ? with * if need more than 1 repetition
    print ("Valid")
else:
    print ("Invalid")


# . ---- any character except a newline
# * ---- 0 or more repetitions
# + ---- 1 or more repetitions
# ? ---- 0 or 1 repetition
# {m} ---- m repetions, where m is an integer
# {m,n} ---- m-n repetions, where n is an integer

# ^ ---- matches the start of the string
# $ ---- matches the end of the string

# [] ---- set of character
# [^] ---- cannot match any of these characters

# \w ---- word chacracter (alnum) [a-zA-Z0-9_] including underscores
# \W ---- not a word character
# \d ---- decimal digit [0-9]
# \D ---- not a decimal digit
# \s ---- whitespace characters
# \S ---- not a whitespace character

# A|B ---- either A or B
# (...) ---- a group or capturing group(1,2,3) and can be a return value from re.search function
# (?:...) ---- not-capturing version (grouped but dont capture)

# re.IGNORECASE ---- treat case insensitive
# re.MULTILINE ---- match different lines of texts
# re.DOTALL ---- configure . + new line
