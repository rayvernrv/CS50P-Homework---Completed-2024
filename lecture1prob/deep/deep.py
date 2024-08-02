#Reply "Yes" if user input answer related to 42, else reply No
ans = input ("What is the Answer to the Great Question of Life, the Universe and Everything? ").lower().strip().replace (" ","").replace ("-","")

#I realised it could be more fool proof to replace any spaces or dashes in between the input using .replace str method

if ans == "42" or ans == "fortytwo" or ans == "forty 2":
    print ("Yes")
else:
    print ("No")
