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

explaination = """Sea Battle is essentially "Battleship" with a few rule changes. Each player has ships varying from lengths 1 to 4, and they can be placed on the board vertically or horizontally. Ships cannot be within 1 tile of one another. Each player picks a tile to attack. If they miss, their turn is over, but if they hit a ship, they keep going until they miss. The game is over once one player destroys all the other player's ships.

You will be asked which dimension you want to make the board. Sea Battle has 8x8, 9x9, and 10x10 modes available. Each mode has a different set of ships.

Before each turn, the best moves will be shown on the board in blue. To see the scores that the A.I. has calculated for each location on the board, you can type d to show the space densities table. The number mostly corresponds to how many ways a ship could be placed at that location, so a higher number means that the space is more likely to have a ship. The AI also takes into account the number of spaces that would be cleared if the spot were to result in a hit/sink. While only the optimal move(s) will be shown on the board display, the densities table uses a color gradient so that you can easily see the good locations on the board if you do not wish to play in one of the optimal spaces. At the beginning of a 10x10 game.

As the game progresses, ships will be destroyed and removed from the ship counter. This will also affect how the densities are computed. A 10x10 match in mid-game is shown below, as well as the corresponding space densities table. The white - represent open spaces (available moves), the red represent misses, the yellow H represent hits, and the green D represent destroyed ships.

After the player selects a move, they will be asked whether the move resulted in a miss, hit, or sink. It will then update the board and space densities accordingly. If the player chooses a space that is not in the optimal move set, the player will be asked to confirm that they meant to choose that location. This is to prevent accidental incorrect input."""


print(Fore.LIGHTGREEN_EX + Style.BRIGHT + "Explaination:" + Style.RESET_ALL)
print("")
printing(Fore.CYAN + Style.BRIGHT + explaination + Style.RESET_ALL)