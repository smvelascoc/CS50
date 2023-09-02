name = input("Camel name: ")
n = len(name)

for i in range (0,n):
    if name[i].isupper():
        print("_" + name[i].lower(), end="")
    else:
        print(name[i], end="")

print("\n",end="")