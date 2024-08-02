import sys
#argv: argument vector, it's a list, basically reading EACH word

if len(sys.argv) < 2: #or len (sys.argv) > 2
    sys.exit ("Wrong arguments") #sys.exit if condition not met, and end the program

print ("Hello, my name is", sys.argv[1])

print ("------------------------------------------------")

for arg in sys.argv[1:]: #start from index 1 of input
    print ("Hello, my name is", arg[1:]) #start from 2nd character (index [1])

