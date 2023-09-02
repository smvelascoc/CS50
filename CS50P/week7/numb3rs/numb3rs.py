import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    matches = re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip)
    if matches:
        for i in range(1,5):
            try:
                if not validate_range(int(matches.group(i))):
                    return False
            except ValueError:
                return False
        return True
    else:
        return False

def validate_range(n):
    if 0 <= n <= 255:
        return True
    else:
        return False

if __name__ == "__main__":
    main()