def main():
    menu = {
    "baja taco": 4.00,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "qzeeuesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00
    }

    t = 0

    while True:
        try:
            item = input("Item: ")
            t= t + menu[item.lower()]
        except KeyError:
            pass
        except EOFError:
            print("\n")
            break
        else:
            print(f"Total: ${t:.2f}")


main()