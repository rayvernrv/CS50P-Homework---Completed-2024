import random
import sys
from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()  # list of fonts, assigned to "fonts"

if len(sys.argv) == 3:
    if sys.argv[2] in fonts:
        figlet.setFont(font=sys.argv[2])
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            user_input = input("Input: ")
            print("Output:", figlet.renderText(user_input))
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")

elif len(sys.argv) == 1:
    randomfont = random.choice(fonts)
    figlet.setFont(font=randomfont)
    user_input = input("Input: ")
    print("Output:", figlet.renderText(user_input))

else:
    sys.exit("Invalid usage")
