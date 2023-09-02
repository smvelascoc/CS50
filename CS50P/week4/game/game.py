import random

while True:
    try:
        n=int(input("Level: "))
    except ValueError:
        pass
    else:
        if n > 0:
            break

number = random.randint(1,n)

while True:
    try:
        g=int(input("Guess: "))
    except ValueError:
        pass
    else:
        if g > number:
            print("Too large!")
        if g < number and g > 0:
            print("Too small!")
        if g == number:
            print("Just right!")
            break