def main():
    while True:
        fuel = input("Fraction: ")

        try:
            print(gauge(convert(fuel)))
            break
        except ValueError:
            #print("ValueError")
            pass
        except ZeroDivisionError:
            #print("ZeroDivisionError")
            pass

def convert(fraction):
    i = fraction.find("/")

    n = int(fraction[0:i])
    d = int(fraction[i+1:len(fraction)])

    if n > d:
        raise ValueError
    else:
        return int(round(n/d*100))


def gauge(percentage):
    #f = int(round(a/b*100))
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return str(percentage)+"%"


if __name__ == "__main__":
    main()
