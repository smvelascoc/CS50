import re
import sys


def main():
    try:
        print(convert(input("Hours: ")))
    except ValueError:
        sys.exit("ValueError")


def convert(s):
    matches = re.search(r"^((?:\d+)(?::\d\d)? (?:[A|P]M)) to ((?:\d+)(?::\d\d)? (?:[A|P]M))",s.strip(),re.IGNORECASE)
    if matches:
        start = matches.group(1)
        end = matches.group(2)
        #print(start)
        #print(end)
        try:
            return str(f"{convert_hour(start)} to {convert_hour(end)}")
        except ValueError:
            raise ValueError
    else:
        raise ValueError

def convert_hour(hour):
    matches = re.search(r"^(\d+):?(\d\d)? ([A|P]M)", hour, re.IGNORECASE)
    # Check hours
    h = int(str(matches.group(1)))
    if h > 12:
        #print("This error wil be raised")
        raise ValueError
    # Check minutes
    if matches.group(2) == None:
        m = 0
    else:
        m = int(str(matches.group(2)))

    if m > 59:
        #print("Erro in minute will be raised")
        raise ValueError

    # Check meridian
    mer = matches.group(3)

    #Conversion hour
    if mer.startswith("P"):
        if h < 12:
            h = (h + 12)
    else:
        if h == 12:
            h = 0

    #Return value
    return f"{h:02}:{m:02}"

if __name__ == "__main__":
    main()