def main ():
#Ask user to input a time. Can be 12-hour or 24-hour format
    current_time = input ("What time is it? ")
#If user input with 12-hour format
    if current_time.replace (".","").endswith ("pm") or current_time.replace (".","").endswith ("am"):
        new_time2 = convert2 (current_time)
        if 7 <= new_time2 <= 8:
            print ("Breakfast Time")
        elif 24 <= new_time2 <= 25:
            print ("Lunch Time")
        elif 18 <= new_time2 <= 19:
            print ("Dinner Time")
#If user input with 24-hour format
    else:
        new_time = convert (current_time)
        if 7 <= new_time <= 8:
            print ("Breakfast Time")
        elif 12 <= new_time <= 13:
            print ("Lunch Time")
        elif 18 <= new_time <= 19:
            print ("Dinner Time")

#Define convert function for 24-hour format
def convert (time):
    hours, minutes = time.split (":")
    converted_time =  round (float (hours) + float (minutes)/60,2)
    return converted_time

#Define convert function for 12-hour format
def convert2 (time2):
    hours2, minutes2 = time2.split (":")
    mins2, am_pm = minutes2.split (" ")
    am_pm = am_pm.strip ().replace (".","")
#if p.m. is input, + 12. need to consider 12pm too, it will become 24
    if am_pm == "pm":
        converted_time2 = int (12) + round (float (hours2) + float (mins2)/60,2)
    else:
        converted_time2 =  round (float (hours2) + float (mins2)/60,2)
    return converted_time2

if __name__ == "__main__":
    main ()
