import time
import os
from colorama import Fore, Style
from sys import stdout
from getkey import getkey
from ansi.color import fg
from ansi import cursor

def intro():
    return """███ █▄┼▄█ ███ ██▄' ███ ┼┼ █▄┼▄█ ███ █┼┼█ ███ ████ ███ █▄┼▄█ ███ ███.\n█┼█ █┼█┼█ █▄┼ █┼█' █▄▄ ┼┼ █┼█┼█ ┼█┼ ██▄█ ┼█┼ █┼▄▄ █▄█ █┼█┼█ █▄┼ █▄▄▀\n█▄█ █┼┼┼█ █▄▄ ███' ▄▄█ ┼┼ █┼┼┼█ ▄█▄ █┼██ ▄█▄ █▄▄█ █┼█ █┼┼┼█ █▄▄ ▄▄█ ▀"""

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

def game(choices):
  global pos
  pointer = fg.boldblue('>')
  for choice in enumerate(choices):
    text = f'  {choice[0]+1}. {choice[1]}'
    if choice[0] == 0:
      text = fg.bold(text)
    print(text)
  print(cursor.hide()+cursor.up()*(len(choices))+pointer, end='')
  stdout.flush()

  pos = 1
  while 1:
    key = getkey()
    text = f'  {pos}. {choices[pos-1]}'
    if (key == '\x1b[A' or key == 'w') and pos > 1:
      pos -= 1
      print(f'\r{text}\r' + cursor.up() + pointer + \
            fg.bold(f' {pos}. {choices[pos-1]}'), end = '')
    elif (key == '\x1b[B' or key == 's') and pos < len(choices):
      pos += 1
      print(f'\r{text}\r' + cursor.down() + pointer + \
            fg.bold(f' {pos}. {choices[pos-1]}'), end = '')
    elif key == '\n':
      print(cursor.down()*(len(choices)-pos)+cursor.show())
      return pos, choices[pos-1]
    elif key.isdecimal():
      number = int(key)
      if 0 < number <= len(choices):
        print(cursor.down()*(len(choices)-pos)+cursor.show())
        return number, choices[number-1]
    stdout.flush()

print(intro())
print("")
print('Enter your choice:')
print("Pick on of the games! For more info visit " + Fore.BLACK + Style.BRIGHT + "readme.md " + Style.RESET_ALL + "or" + Fore.GREEN + Style.BRIGHT + " Game Explainations" + Style.RESET_ALL)
games=game([Fore.RED + 'Connect4' + Style.RESET_ALL, Fore.YELLOW + 'Gomoku' + Style.RESET_ALL, Fore.BLUE + 'Othello' + Style.RESET_ALL, Fore.MAGENTA + 'Tic Tac Toe' + Style.RESET_ALL, Fore.RED + 'Wordle' + Style.RESET_ALL, Fore.CYAN + 'Sea Battle (TOOL)' + Style.RESET_ALL, Fore.GREEN + 'Mancala (Avalanche) (TOOL)' + Style.RESET_ALL, Fore.WHITE + 'Word Bites (TOOL)' + Style.RESET_ALL, Fore.YELLOW + 'Word Hunt (TOOL)' + Style.RESET_ALL, Fore.GREEN + Style.BRIGHT + 'Game Explainations' + Style.RESET_ALL])

print(games[1])

if games[1] == "Connect4":
    print("You chose " + Fore.RED + "Connect 4." + Style.RESET_ALL)
    time.sleep(1)
    clearConsole()
    print(Fore.GREEN + "Loading game..." + Style.RESET_ALL)
    time.sleep(1)
    import progress_bar.progress_bar
    clearConsole()
    import connect_4.connect4_client
        
elif games[1] == "Gomoku":
    print("You chose " + Fore.YELLOW + "Gomoku." + Style.RESET_ALL)
    time.sleep(1)
    clearConsole()
    print(Fore.GREEN + "Loading game..." + Style.RESET_ALL)
    time.sleep(1)
    import progress_bar.progress_bar
    clearConsole()
    import gomoku.gomoku_client

elif games[1] == "Othello":
    print("You chose " + Fore.BLUE + "Othello." + Style.RESET_ALL)
    time.sleep(1)
    clearConsole()
    print(Fore.GREEN + "Loading game..." + Style.RESET_ALL)
    time.sleep(1)
    import progress_bar.progress_bar
    clearConsole()
    import othello.othello_client

elif games[1] == "Tic Tac Toe":
    print("You chose " + Fore.MAGENTA + "Tic Tac Toe." + Style.RESET_ALL)
    time.sleep(1)
    clearConsole()
    print(Fore.GREEN + "Loading game..." + Style.RESET_ALL)
    time.sleep(1)
    import progress_bar.progress_bar
    clearConsole()
    import tic_tac_toe.tictactoe_client


elif games[1] == "Wordle":
    print("You chose " + Fore.RED + "Wordle" + Style.RESET_ALL)
    time.sleep(1)
    clearConsole()
    print(Fore.GREEN + "Loading game..." + Style.RESET_ALL)
    time.sleep(1)
    import progress_bar.progress_bar
    clearConsole()
    import wordle.wordle_main
  
elif games[1] == "Sea Battle (TOOL)":
    print("You chose " + Fore.CYAN + "Sea Battle (TOOL)" + Style.RESET_ALL)
    time.sleep(1)
    clearConsole()
    print(Fore.GREEN + "Loading game..." + Style.RESET_ALL)
    time.sleep(1)
    import progress_bar.progress_bar
    clearConsole()
    import seabattle.seabattle

elif games[1] == "Mancala (Avalanche) (TOOL)":
    print("You chose " + Fore.GREEN + "Mancala (Avalanche) (TOOL)" + Style.RESET_ALL)
    time.sleep(1)
    clearConsole()
    print(Fore.GREEN + "Loading tool..." + Style.RESET_ALL)
    time.sleep(1)
    import progress_bar.progress_bar
    clearConsole()
    import mancala_avalanche.mancalaavalanche
        
elif games[1] == "Word Bites (TOOL)":
    print("You chose " + Fore.WHITE + "Word Bites (TOOL)" + Style.RESET_ALL)
    time.sleep(1)
    clearConsole()
    print(Fore.GREEN + "Loading tool..." + Style.RESET_ALL)
    time.sleep(1)
    import progress_bar.progress_bar
    clearConsole()
    import holder
        
elif games[1] == "Word Hunt (TOOL)":
    print("You chose " + Fore.YELLOW + "Word Hunt (TOOL)" + Style.RESET_ALL)
    time.sleep(1)
    clearConsole()
    print(Fore.GREEN + "Loading tool..." + Style.RESET_ALL)
    time.sleep(1)
    import progress_bar.progress_bar
    clearConsole()
    import holder

elif games[1] == "Game Explainations":
    print("You chose " + Style.BRIGHT + Fore.GREEN + "Game Explainations" + Style.RESET_ALL)
    time.sleep(1)
    clearConsole()
    print(Fore.GREEN + "Loading Explainations..." + Style.RESET_ALL)
    time.sleep(1)
    import progress_bar.progress_bar
    clearConsole()
    import explanations.Explainations
  
else:
    print(Fore.RED + Style.BRIGHT + "Invalid input. Somehow..." + Style.RESET_ALL)
    time.sleep(1)
    clearConsole()
    exit(0)