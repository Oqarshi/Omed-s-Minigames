import time
import os
from colorama import Fore, Style
import random

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

def intro():
    return """
███████╗██╗░░██╗██████╗░██╗░░░░░░█████╗░██╗███╗░░██╗░█████╗░████████╗██╗░█████╗░███╗░░██╗░██████╗
██╔════╝╚██╗██╔╝██╔══██╗██║░░░░░██╔══██╗██║████╗░██║██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║██╔════╝
█████╗░░░╚███╔╝░██████╔╝██║░░░░░███████║██║██╔██╗██║███████║░░░██║░░░██║██║░░██║██╔██╗██║╚█████╗░
██╔══╝░░░██╔██╗░██╔═══╝░██║░░░░░██╔══██║██║██║╚████║██╔══██║░░░██║░░░██║██║░░██║██║╚████║░╚═══██╗
███████╗██╔╝╚██╗██║░░░░░███████╗██║░░██║██║██║░╚███║██║░░██║░░░██║░░░██║╚█████╔╝██║░╚███║██████╔╝
╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝╚═╝╚═╝░░╚══╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝╚═════╝░"""

while True:
    print(intro())
    print("")
    game_choice = input("Which game would you like an explaination for?\n"
                        "1: " + Fore.RED + "Connect 4" + Style.RESET_ALL + "\n"
                        "2: " + Fore.YELLOW + "Gomoku (5 in a row)" + Style.RESET_ALL + "\n"
                        "3: " + Fore.BLUE + "Othello" + Style.RESET_ALL + "\n"
                        "4: " + Fore.CYAN + "Sea Battle" + Style.RESET_ALL + "\n"
                        "5: " + Fore.MAGENTA + "Tic Tac Toe (3 in a row)" + Style.RESET_ALL + "\n"
                        "6: " + Fore.RED + "Wordle TOOL" + Style.RESET_ALL + "\n"
                        "" + Fore.WHITE + "---------------------------" + Style.RESET_ALL + "\n"
                        "7: " + Fore.GREEN + "Mancala (Avalanche) TOOL" + Style.RESET_ALL + "\n"
                        "8: " + Fore.WHITE + "Word Bites TOOL" + Style.RESET_ALL + "\n"
                        "9: " + Fore.YELLOW + "Word Hunt TOOL" + Style.RESET_ALL + "\n"
                        "Enter a number between 1 and 9: ")
    
    if game_choice == "1":
        print("You chose " + Fore.RED + "Connect 4." + Style.RESET_ALL)
        time.sleep(1)
        clearConsole()
        print(Fore.GREEN + "Loading explaination..." + Style.RESET_ALL)
        time.sleep(1)
        import progress_bar.progress_bar
        clearConsole()
        import explanations.Connect_4
        break
        
    elif game_choice == "2":
        print("You chose " + Fore.YELLOW + "Gomoku." + Style.RESET_ALL)
        time.sleep(1)
        clearConsole()
        print(Fore.GREEN + "Loading explaination..." + Style.RESET_ALL)
        time.sleep(1)
        import progress_bar.progress_bar
        clearConsole()
        import explanations.Gomoku
        break

    elif game_choice == "3":
        print("You chose " + Fore.BLUE + "Othello." + Style.RESET_ALL)
        time.sleep(1)
        clearConsole()
        print(Fore.GREEN + "Loading explaination..." + Style.RESET_ALL)
        time.sleep(1)
        import progress_bar.progress_bar
        clearConsole()
        import explanations.Othello
        break

    elif game_choice == "4":
        print("You chose " + Fore.CYAN + "Sea Battle." + Style.RESET_ALL)
        time.sleep(1)
        clearConsole()
        print(Fore.GREEN + "Loading explaination..." + Style.RESET_ALL)
        time.sleep(1)
        import progress_bar.progress_bar
        clearConsole()
        import explanations.Sea_Battle
        break

    elif game_choice == "5":
        print("You chose " + Fore.MAGENTA + "Tic Tac Toe." + Style.RESET_ALL)
        time.sleep(1)
        clearConsole()
        print(Fore.GREEN + "Loading explaination..." + Style.RESET_ALL)
        time.sleep(1)
        import progress_bar.progress_bar
        clearConsole()
        import explanations.Tic_Tac_Toe
        break

    elif game_choice == "6":
        print("You chose " + Fore.RED + "Wordle TOOL." + Style.RESET_ALL)
        time.sleep(1)
        clearConsole()
        print(Fore.GREEN + "Loading explaination..." + Style.RESET_ALL)
        time.sleep(1)
        import progress_bar.progress_bar
        clearConsole()
        import explanations.Wordle_Tool
        break

    elif game_choice == "7":
        print("You chose " + Fore.GREEN + "Mancala (Avalanche) TOOL." + Style.RESET_ALL)
        time.sleep(1)
        clearConsole()
        print(Fore.GREEN + "Loading explaination..." + Style.RESET_ALL)
        time.sleep(1)
        import progress_bar.progress_bar
        clearConsole()
        import explanations.Mancala_Avalanche
        break
        
    elif game_choice == "8":
        print("You chose " + Fore.WHITE + "Word Bites TOOL." + Style.RESET_ALL)
        time.sleep(1)
        clearConsole()
        print(Fore.GREEN + "Loading explaination..." + Style.RESET_ALL)
        time.sleep(1)
        import progress_bar.progress_bar
        clearConsole()
        import explanations.Word_Bites
        break
        
    elif game_choice == "9":
        print("You chose " + Fore.YELLOW + "Word Hunt TOOL." + Style.RESET_ALL)
        time.sleep(1)
        clearConsole()
        print(Fore.GREEN + "Loading explaination..." + Style.RESET_ALL)
        time.sleep(1)
        import progress_bar.progress_bar
        clearConsole()
        import explanations.Word_Hunt
        break

    else:
        print("Invalid input. Please enter a number between 1 and 9.")
        time.sleep(1)
        clearConsole()
