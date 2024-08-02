def main():
#Ask user to input a time in 12-hour format
    current_time = input ("What time is it? ")
    new_time = convert (current_time)

#Prompt different answer depending on the time
    if 7 <= new_time <= 8:
        print ("Breakfast Time")
    elif 24 <= new_time <= 25:
        print ("Lunch Time")
    elif 18 <= new_time <= 19:
        print ("Dinner Time")

def convert(time):
    hours, minutes = time.split (":")
    mins, am_pm = minutes.split (" ")
    am_pm = am_pm.strip ().replace (".","")
#if p.m. is input, + 12. need to consider 12pm too, it will become 24
    if am_pm == "pm":
        converted_time = int (12) + round (float (hours) + float (mins)/60,2)
    else:
        converted_time =  round (float (hours) + float (mins)/60,2)
    return converted_time

if __name__ == "__main__":
    main ()
"""
def main():
#Ask user to input a time in 24 hour format
    current_time = input ("What time is it? ")
    new_time = convert (current_time)
#Prompt different answer depending on the time
    if 7 <= new_time <=8:
        print ("Breakfast Time")
    elif 12 <= new_time <=13:
        print ("Lunch Time")
    elif 18 <= new_time <=19:
        print ("Dinner Time")

def convert(time):
    hours, minutes = time.split (":")
    converted_time =  round (float (hours) + float (minutes)/60,2)
    return converted_time

if __name__ == "__main__":
    main ()
"""
