op=input("Operation: ")

x,y,z=op.split(" ")

match y:
    case "+":
        print(f'{float(x)+float(z):.1f}')
    case "-":
        print(f'{float(x)-float(z):.1f}')
    case "*":
        print(f'{float(x)*float(z):.1f}')
    case "/":
        print(f'{float(x)/float(z):.1f}')