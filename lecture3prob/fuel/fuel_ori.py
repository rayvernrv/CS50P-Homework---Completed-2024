while True:
    try:
        fuel = input ("Fraction: ")
        fuel = fuel.split("/")
        conv_to_perc = (int (fuel[0]) / int (fuel[1]))*100
    except (ValueError,ZeroDivisionError):
        pass
    else:
        if int(fuel[0]) < int(fuel[1]) or int(fuel[0]) == int(fuel[1]):
            break

if 1 < conv_to_perc < 99:
    print (f"{conv_to_perc:.0f}%")
elif 99 <= conv_to_perc <= 100:
    print ("F")
elif 0 <= conv_to_perc <= 1:
    print ("E")
