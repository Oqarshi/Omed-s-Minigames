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

explaination = """In Gomoku, the objective is to get 5 of your pieces to line up in succession. The player can choose any spot on the board to play their piece. Each player places one piece per turn. One easy way to think of this is that it is basically Tic-Tac-Toe, except it is played on a much bigger board, and you need 5 pieces in a row to win instead of 3.

You will be asked how big you want the board to be. This number should be an odd number. By default, the board is 13x13. Next, you will be asked which color you want to be (black or white). Whoever is black will go first. Each empty space on the board is represented by a . in the slot. Black and white will be represented by X and O respectively. Your pieces will be colored green, and the AI pieces will be colored red. If it is your turn, you will enter the name of the spot you want to play (e.g. E7). Then, you will be prompted to press enter to have the A.I. play its best move. At any point, if you want to quit, you can simply type q as your move input."""


print(Fore.LIGHTGREEN_EX + Style.BRIGHT + "Explaination:" + Style.RESET_ALL)
print("")
printing(Fore.YELLOW + Style.BRIGHT + explaination + Style.RESET_ALL)