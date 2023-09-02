names = list()

while True:
    try:
        names.append(input("Name: "))
    except EOFError:
        print("\nAdieu, adieu, to ", end = '')
        if len(names) > 2:
            for n in range(0,len(names)-1):
                print(names[n], end = ', ')

            print("and " + names[len(names)-1])
        elif len(names) == 2:
            print(names[0] + " and " + names[1])
        else:
            print(names[0])

        break