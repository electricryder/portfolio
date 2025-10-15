from datetime import date, timedelta
from validator_collection import checkers
import sys
import inflect
import re

"""class BirthDate:
    def __init__(self, year, month, day, complete):
        self.year = year
        self.month = month
        self.day = day
        self.complete = complete"""


def main():
    inpt = input("Date of Birth: ")
    lived_minutes(inpt)


def get_birth_date(inpt):
    if checkers.is_date(inpt):
        year = int(inpt.split("-")[0])
        month = int(inpt.split("-")[1])
        day = int(inpt.split("-")[2])
        return date(year, month, day)
    else:
        sys.exit("Invalid date")


def lived_minutes(date_str):
    date = get_birth_date(date_str)
    today_date = date.today()
    day_difference = today_date - date
    num_to_wor(day_difference.days * 24 * 60)


def num_to_wor(num):
    p = inflect.engine()
    words = p.number_to_words(num, wantlist=True)
    for c, word in enumerate(words):
        word = re.sub(" and ", " ", word)
        if c == 0:
            print(word.capitalize(), end=", ")
        elif c != len(words) - 1:
            print(word, end=", ")
        else:
            print(word, "minutes")


if __name__ == "__main__":
    main()
