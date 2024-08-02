def main():
    while True:
        try:
            user_fraction = input ("Fraction: ")
            if int(user_fraction[2]) == 0:
                raise ZeroDivisionError
            elif int(user_fraction[0]) > int(user_fraction[2]):
                raise ValueError
            else:
                break
        except (ValueError,ZeroDivisionError):
            pass
    percentage = convert(user_fraction)
    print (gauge(percentage))


def convert(fraction):
        value = (int (fraction[0]) / int (fraction[2]))*100
        return int (value)


def gauge(percentage):
    if 1 < percentage < 99:
        return f"{percentage:.0f}%"
    elif 99 <= percentage <= 100:
        return "F"
    elif 0 <= percentage <= 1:
        return "E"


if __name__ == "__main__":
    main()


