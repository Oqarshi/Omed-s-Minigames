import time
from colorama import Fore, Style

def printing(text, delay=0.001):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def intro():
    return """
███████╗██╗░░██╗██████╗░██╗░░░░░░█████╗░██╗███╗░░██╗░█████╗░████████╗██╗░█████╗░███╗░░██╗░██████╗
██╔════╝╚██╗██╔╝██╔══██╗██║░░░░░██╔══██╗██║████╗░██║██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║██╔════╝
█████╗░░░╚███╔╝░██████╔╝██║░░░░░███████║██║██╔██╗██║███████║░░░██║░░░██║██║░░██║██╔██╗██║╚█████╗░
██╔══╝░░░██╔██╗░██╔═══╝░██║░░░░░██╔══██║██║██║╚████║██╔══██║░░░██║░░░██║██║░░██║██║╚████║░╚═══██╗
███████╗██╔╝╚██╗██║░░░░░███████╗██║░░██║██║██║░╚███║██║░░██║░░░██║░░░██║╚█████╔╝██║░╚███║██████╔╝
╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝╚═╝╚═╝░░╚══╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝╚═════╝░"""

print(intro())
print("")

explaination = """You will be prompted about which display mode you would like to use: Diagram Mode, or List Mode. Typing i will give you more information about each of them.
After this, you will be asked to input the letter tiles in 3 different categories: single letters, horizontal pieces, and vertical pieces. Then, the program will calculate and display the best piece combinations.

Diagram Mode:
Diagram mode will display each word one at a time, along with a visual representation of how to arrange the board pieces. Longer words will be displayed first."""


print(Fore.LIGHTGREEN_EX + Style.BRIGHT + "Explaination:" + Style.RESET_ALL)
print("")
printing(Fore.WHITE + Style.BRIGHT + explaination + Style.RESET_ALL)