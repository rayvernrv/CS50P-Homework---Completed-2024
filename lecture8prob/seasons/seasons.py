# My original solution that work, but not optimized
# too many function related to class but calling it outside

import inflect
import sys

from datetime import date


class Time:
    def __init__(self, year=0, month=0, day=0):
        self.year = year
        self.month = month
        self.day = day

    def get_today():
        return date.today()

    @staticmethod
    def get_dob():
        try:
            year, month, day = input("Date of Birth: ").split("-")
            year = int(year)
            month = int(month)
            day = int(day)
            return date(year, month, day)
        except ValueError:
            sys.exit("Invalid date")

    def __sub__(self, other):
        year = self.year - other.year
        month = self.month - other.month
        day = self.day - other.day
        return Time(year, month, day)


def main():
    dob = Time.get_dob()
    today = Time.get_today()
    delta_mins = convert_mins(today - dob)
    print(convert_text(delta_mins))

# convert day to mins
def convert_mins(m):
    minutes = m.days * 24 * 60
    return minutes


def convert_text(n):
    p = inflect.engine()
    return f"{(p.number_to_words(n, andword="")).capitalize()} minutes"


if __name__ == "__main__":
    main()
