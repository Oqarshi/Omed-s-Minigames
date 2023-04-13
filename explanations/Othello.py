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

explaination = """The overall objective of the game is to end the game with more pieces on the board than the opponent. Each turn, a player will play one piece. A player can only play a piece in spaces that trap enemy pieces between this new piece, and an existing friendly piece on the board, with no empty spaces in between. The enemy pieces between this new piece and the nearest existing friendly piece are "captured," and converted to friendly pieces. This applies in any direction (horizontal, vertical, diagonal).

Once you do this, you will see some info about how to interact with the tool, further explained in the Gameplay Features section. You will be asked if you would like to see the rules, and then you will be prompted to choose which color you want to be, BLACK (0) or WHITE (O). Whoever is BLACK will go first. You will then be prompted to either enter your move, or press enter for the A.I. to play."""


print(Fore.LIGHTGREEN_EX + Style.BRIGHT + "Explaination:" + Style.RESET_ALL)
print("")
printing(Fore.BLUE + Style.BRIGHT + explaination + Style.RESET_ALL)