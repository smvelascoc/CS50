def main():
    months=[
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    #  Translate
    while True:
        try:
            date = input("Date: ")
            if date.find("/") != -1:
                m,d,y=date.split("/")

            if (date.find(" ") != -1) and (date.find(",") != -1):

                #Month
                month = date.split(" ", maxsplit=1)
                month[0] = month[0].capitalize()
                if month[0] in months:
                    m=months.index(month[0])+1
                #Year
                year=date.split(",", maxsplit=1)
                y=year[1]

                # Day
                temp=month[1]
                day=temp.split(",",maxsplit=1)
                d=day[0]

            if (check_day(int(d))) and check_month(int(m)):
                d1 = int(d)
                m1 = int(m)
                y1= int(y)

                print(y1,f"{m1:02}",f"{d1:02}", sep="-")
                break

        except ValueError:
            pass
        except UnboundLocalError:
            pass


def check_day(d):
    if d<=31:
        return True
    else:
        return False


def check_month(m):
    if m<=12:
        return True
    else:
        return False


# Call Main
main()