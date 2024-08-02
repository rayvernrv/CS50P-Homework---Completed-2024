months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        user_date = input ("Date: ")
        month,day,year = user_date.split("/")
        if 1 <= int (month) <= 12 and 1 <= int (day) <= 31:
            break
    except ValueError:
        if "/" in user_date or "," not in user_date: #if these 2 conditions is handled by ValueError
            pass #then pass and reprompt
        else:
            month1,day,year = user_date.replace(",","").split()
            if month1 in months and 1 <= int (day) <= 31:
                month = months.index(month1) + 1 #.index assign to the location of month (0 based) + 1
                break
print (f"{int (year)}-{int (month):02}-{int (day):02}")
