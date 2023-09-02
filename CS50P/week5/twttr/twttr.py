def main():
    phrase = input("Input: ")
    print(shorten(phrase))



def shorten(word):
    n=len(word)
    ans=""
    j=0
    for i in range(n):
        if isconsonant(word[i].lower()):
            ans = ans + word[i]
    return ans

def isconsonant(v):
    if v=='a' or v=='e' or v=='i' or v=='o' or v=='u':
        return False
    else:
        return True

if __name__ == "__main__":
    main()