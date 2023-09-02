import random

def main():
    op = list()
    l = get_level()
    score = 0

    for i in range (0,10):
        couple = dict()
        couple["X"] = generate_integer(l)
        couple["Y"] = generate_integer(l)
        op.append(couple)

    for i in range(0,len(op)):
        life = 3
        while True:
            try:
                if life == 0:
                    raise ValueError

                x = op[i]["X"]
                y  = op[i]["Y"]
                r = int(input(f"{x} + {y} = "))
                if (r == (x + y)):
                    score = score + 1
                    break
                else:
                    raise ValueError
            except ValueError:
                if life == 0:
                    print(f"{x} + {y} = {x+y}")
                    break
                else:
                    life = life -1
                    print("EEE")

    print(f"Score: {score}")

def get_level():
    while True:
        try:
            l = int(input("Level: "))
        except ValueError:
            pass
        else:
            if (l > 0) and (l < 4):
                return l


def generate_integer(level):
    if (level > 0) and ( level < 4):
        if level == 1:
            return random.randint(0,9)
        else:
            return random.randint(pow(10,level-1), pow(10,level)-1)
    else:
        raise ValueError


if __name__ == "__main__":
    main()