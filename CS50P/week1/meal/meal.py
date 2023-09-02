def main():
    tm = convert(input("What time is it? "))

    if 7 <= tm <= 8:
            print("breakfast time")
    elif 12 <= tm <= 13:
            print("lunch time")
    elif  18 <= tm <= 19:
            print("dinner time")


def convert(time):
    h,m=time.split(":")
    return float(h) + float(m)/60


if __name__ == "__main__":
    main()