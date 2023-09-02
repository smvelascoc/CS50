import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    matches = re.search(r"src=\"https?://(?:www\.)?youtube\.com/embed/(.+?)\"", s, re.IGNORECASE)
    if matches:
        return (f"https://youtu.be/{matches.group(1)}")
    else:
        return ("None")

if __name__ == "__main__":
    main()