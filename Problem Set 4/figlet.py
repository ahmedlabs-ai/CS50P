from pyfiglet import Figlet
import sys
import random
figlet = Figlet()
fonts = figlet.getFonts()
if len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in fonts:
        fonts = figlet.getFonts()
        figlet.setFont(font = sys.argv[2])
        print("Output:\n ",figlet.renderText(input("Input: ")))
elif len(sys.argv) == 1:
        fonts = figlet.getFonts()
        font = random.choice(fonts)
        figlet.setFont(font = random.choice(fonts))
        print("Output:\n ",figlet.renderText(input("Input: ")))
else:
        sys.exit("Invalid usage")

