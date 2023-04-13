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

explaination = """Mancala Avalanche is a version of Mancala. Players each have 6 pits and a bank. Each pit starts out with a certain number of pieces. The objective of the game is to end up with more pieces in your bank than your opponent. To play your turn, you choose a pit on your side of the board, and pick up all the pieces in that pit. You go down the board, placing one piece in each pit that you pass. You place pieces in your bank, but not your opponent's. If your last piece from that turn ends in your bank, you get another turn. If the last piece ends in another pit, you pick up every piece from that pit, and repeat the process (unless the pit was empty, in which case your turn is over).

You will be prompted for which mode you would like to use (have the moves presented all at once, or one at a time). Next, you will be prompted to enter your side of the board (separated by spaces), followed by the opponent's side of the board. You will be presented with a visualization of the board as you have inputted it. Pressing enter will calculate the best possible move set for that given board. You will then repeat this process until the game is over, or you choose to quit the program."""


print(Fore.LIGHTGREEN_EX + Style.BRIGHT + "Explaination:" + Style.RESET_ALL)
print("")
printing(Fore.GREEN + Style.BRIGHT + explaination + Style.RESET_ALL)