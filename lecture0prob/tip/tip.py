#Calculate the tip when user input the amount and percent to tip
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}") #2d.p.

#Remove $ sign in front and round up to 1 d.p. and convert value to float
def dollars_to_float(d):
    d = d.lstrip ("$")
    return round ((float (d)),1)

#Remove % sign behind and round up to 2 d.p. and convert value to float
def percent_to_float(p):
    p = p.rstrip ("%")
    new_p = round ((float (p) /100),2)
    return new_p

main ()
