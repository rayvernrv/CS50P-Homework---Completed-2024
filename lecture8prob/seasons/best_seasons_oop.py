# True optimized answer using class

import inflect
import sys

from datetime import date


class Time:
    def __init__(self, year=0, month=0, day=0):
        self.year = year
        self.month = month
        self.day = day

    @staticmethod
    def get_today():
        return date.today()

    @staticmethod
    def get_dob():
        try:
            year, month, day = input("Date of Birth: ").split("-")
            return date(int(year), int(month), int(day))
        except ValueError:
            sys.exit("Invalid date")

    @staticmethod
    def convert_mins(delta):
        return delta.days * 24 * 60  # .days is for timedelta object

    @staticmethod
    def convert_text(n):
        p = inflect.engine()
        return f"{(p.number_to_words(n, andword="")).capitalize()} minutes"

    def __sub__(self, other):
        year = self.year - other.year
        month = self.month - other.month
        day = self.day - other.day
        return Time(year, month, day)


def main():
    dob = Time.get_dob()  # timedelta object
    today = Time.get_today()  # timedelta object
    delta_mins = Time.convert_mins(today - dob)  # integer
    print(Time.convert_text(delta_mins))
    print(today-dob)


if __name__ == "__main__":
    main()
