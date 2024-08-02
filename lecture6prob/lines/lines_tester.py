import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # No mins to No mins
    if matches := re.search(r"^((?:0|1)?\d) (AM|PM) to ((?:0|1)?\d) (AM|PM)$", s, re.IGNORECASE):
        s_hour = int(matches.group(1))
        start_ampm = matches.group(2)
        e_hour = int(matches.group(3))
        end_ampm = matches.group(4)
        if s_hour == 12 and start_ampm == "AM":
            s_hour = 0
        if e_hour == 12 and start_ampm == "AM":
            e_hour = 0
        if start_ampm == "PM":
            if s_hour != 12:
                s_hour += 12
        if end_ampm == "PM":
            if e_hour != 12:
                e_hour += 12
        return f"{s_hour:02}:00 to {e_hour:02}:00"

    # No mins to Yes mins
    elif matches := re.search(r"^((?:0|1)?\d) (AM|PM) to ((?:0|1)?\d):([0-5]\d) (AM|PM)$", s, re.IGNORECASE):
        s_hour = int(matches.group(1))
        start_ampm = matches.group(2)
        e_hour = int(matches.group(3))
        e_mins = int(matches.group(4))
        end_ampm = matches.group(5)
        if s_hour == 12 and start_ampm == "AM":
            s_hour = 0
        if e_hour == 12 and start_ampm == "AM":
            e_hour = 0
        if start_ampm == "PM":
            if s_hour != 12:
                s_hour += 12
        if end_ampm == "PM":
            if e_hour != 12:
                e_hour += 12
        return f"{s_hour:02}:00 to {e_hour:02}:{e_mins:02}"

    # Yes mins to No mins
    elif matches := re.search(r"^((?:0|1)?\d):([0-5]\d) (AM|PM) to ((?:0|1)?\d) (AM|PM)$", s, re.IGNORECASE):
        s_hour = int(matches.group(1))
        s_mins = int(matches.group(2))
        start_ampm = matches.group(3)
        e_hour = int(matches.group(4))
        end_ampm = matches.group(5)
        if s_hour == 12 and start_ampm == "AM":
            s_hour = 0
        if e_hour == 12 and start_ampm == "AM":
            e_hour = 0
        if start_ampm == "PM":
            if s_hour != 12:
                s_hour += 12
        if end_ampm == "PM":
            if e_hour != 12:
                e_hour += 12
        return f"{s_hour:02}:{s_mins:02} to {e_hour:02}:00"

    # Yes mins to Yes mins
    elif matches := re.search(r"^((?:0|1)?\d):([0-5]\d) (AM|PM) to ((?:0|1)?\d):([0-5]\d) (AM|PM)$", s, re.IGNORECASE):
        s_hour = int(matches.group(1))
        s_mins = int(matches.group(2))
        start_ampm = matches.group(3)
        e_hour = int(matches.group(4))
        e_mins = int(matches.group(5))
        end_ampm = matches.group(6)
        if s_hour == 12 and start_ampm == "AM":
            s_hour = 0
        if e_hour == 12 and start_ampm == "AM":
            e_hour = 0
        if start_ampm == "PM":
            if s_hour != 12:
                s_hour += 12
        if end_ampm == "PM":
            if e_hour != 12:
                e_hour += 12
        return f"{s_hour:02}:{s_mins:02} to {e_hour:02}:{e_mins:02}"

    else:
        raise ValueError


if __name__ == "__main__":
    main()
