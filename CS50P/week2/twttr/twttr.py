def main():
    phrase = input("Input: ")
    n=len(phrase)

    for i in range(n):
        if isconsonant(phrase[i].lower()):
            print(phrase[i], end="")
    print("")

def isconsonant(v):
    if v=='a' or v=='e' or v=='i' or v=='o' or v=='u':
        return False
    else:
        return True

main()