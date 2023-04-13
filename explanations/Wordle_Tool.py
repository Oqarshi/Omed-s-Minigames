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

explaination = """Wordle is a popular online word-guessing game that tests a player's vocabulary and analytical skills. The game presents players with a hidden five-letter word, and they have six attempts to guess it correctly. Each guess reveals which letters are correct and in the right position with a green box, and which letters are correct but in the wrong position with an yellow box. If a letter is not correct, it appears as a gray box. Based on the feedback from the game, players must eliminate the possibilities and guess the correct word within six tries. The game's simplicity and quick gameplay make it a fun and addictive challenge for word enthusiasts of all ages.

Wordle's gameplay and user interface are straightforward and intuitive, allowing players to jump right in without any instruction or tutorials. The game uses a list of approximately 5000 English words, making the word selection random and diverse, ensuring that each game feels unique. The game's appeal lies in the player's ability to deduce the correct word based on the feedback provided after each guess. With only six attempts, players must weigh the probabilities of each word and eliminate the ones that are not correct."""


print(Fore.LIGHTGREEN_EX + Style.BRIGHT + "Explaination:" + Style.RESET_ALL)
print("")
printing(Fore.RED + Style.BRIGHT + explaination + Style.RESET_ALL)