#If input "Hello", no penalty fees
#If input starts with "H", $20 penalty fees
#Otherwise, $100 penalty fees

greet = input ("Greeting: ").lower().strip().replace (" ","")

if greet.startswith ("hello"):
    print ("$0")
elif greet.startswith ("h"):
    print ("$20")
else:
    print ("$100")
