from datetime import date
import sys
import re
import inflect

def main():
    #Catching date
    birth = input("Date of birth: ")
    try:
        print(minutes(to_date(birth)))
    except ValueError:
        sys.exit("Invalid date")

def to_date(birth):
    match_date = re.search(r"^(\d+)-(\d+)-(\d+)", birth)
    if match_date:
        return date(year = int(match_date.group(1)), month = int(match_date.group(2)), day = int(match_date.group(3)))
    else:
        raise ValueError

def minutes(day):
    #Testing date and printing
    t = date.today() - day
    if t.days >= 0:
        p=inflect.engine()
        return str((p.number_to_words(t.days * 24 * 60, andword="") + " minutes").capitalize())
    else:
        raise ValueError

if __name__ == "__main__":
    main()