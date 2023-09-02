def main():
    while True:
        fuel = input("Fraction: ")
        i = fuel.find("/")

        try:
            n = int(fuel[0:i])
            d = int(fuel[i+1:len(fuel)])
            n/d
        except ValueError:
            #print("ValueError")
            pass
        except ZeroDivisionError:
            #print("ZeroDivisionError")
            pass
        else:
            if (n<=d):
                print(Fuel_Print(n,d))
                break

def Fuel_Print(a,b):
    f = int(round(a/b*100))
    if f >= 99:
        return "F"
    elif f <= 1:
        return "E"
    else:
        return str(f)+"%"


main()