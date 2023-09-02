grocery = dict()

while True:
    try:
        it=input()
        grocery[it.upper()] = grocery[it.upper()] + 1
    except KeyError:
        grocery[it.upper()] = 1
    except EOFError:
        for i in sorted(grocery.keys()):
            print(grocery[i], i)
        break