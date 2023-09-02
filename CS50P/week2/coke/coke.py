c=50
while True:
    n=int(input("Insert a coin"))
    if n==5 or n==10 or n==25:
        c=c-n

    if c > 0:
        print("Amount due: " + str(c))
    else:
        print("Change owed: " + str(-c))
        break