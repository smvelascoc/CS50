import random
from pyfiglet import Figlet
import sys


figlet = Figlet()
fonts = figlet.getFonts()

#Check arguments
if len(sys.argv) == 1:
    f=figlet.setFont(font=random.choice(fonts))
    pass
elif len(sys.argv) == 3:
    #Check font
    if sys.argv[1] == '-f' or sys.argv[1] == '--font':
        if sys.argv[2] in fonts:
            f=figlet.setFont(font=sys.argv[2])
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")
    pass
else:
    sys.exit("Invalid usage")

print(figlet.renderText(input("Input: ")))