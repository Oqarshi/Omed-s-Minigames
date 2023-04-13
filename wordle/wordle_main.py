import random
import numpy as np
import pandas as pd
import os
from colorama import Fore, Style
from tqdm import tqdm

from wordle.bot import Agent
from wordle.wordle import Wordle

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

def intro():
    return """███ █▄┼▄█ ███ ██▄' ███ ┼┼ █▄┼▄█ ███ █┼┼█ ███ ████ ███ █▄┼▄█ ███ ███.\n█┼█ █┼█┼█ █▄┼ █┼█' █▄▄ ┼┼ █┼█┼█ ┼█┼ ██▄█ ┼█┼ █┼▄▄ █▄█ █┼█┼█ █▄┼ █▄▄▀\n█▄█ █┼┼┼█ █▄▄ ███' ▄▄█ ┼┼ █┼┼┼█ ▄█▄ █┼██ ▄█▄ █▄▄█ █┼█ █┼┼┼█ █▄▄ ▄▄█ ▀"""
  
ROWS = 6
LETTERS = 5

w_bank = pd.read_csv("wordle/data/words.csv")
w_bank = w_bank[w_bank["words"].str.len() == LETTERS]
w_bank["words"] = w_bank["words"].str.upper()
print(intro())
print("")
control = input(
    "What would you like to do?\n\n-Test Solver [T]\n-Game Assist [A]\n-Play Game   [P]\n\n"
)
if "T" in str(control).upper() or "P" in str(control).upper():
    if "P" in str(control).upper():
        clearConsole()
        print(intro())
        print("")
        print(Fore.GREEN + Style.BRIGHT + "PLAY GAME SELECTED\n---------------------" + Style.RESET_ALL)
    else:
        clearConsole()
        print(intro())
        print("")
        print(Fore.RED + Style.BRIGHT + "TEST SOLVER SELECTED\n---------------------\n" + Style.RESET_ALL)
        GAMES = int(input(Fore.RED + "Number of games to test the solver: " + Style.RESET_ALL))
    results = []
    if "P" in str(control).upper():
        silent = True
        GAMES = 1
    else:
        silent = False
    for _ in tqdm(range(GAMES), desc="GAMES", disable=silent):
        word = random.choice(w_bank["words"].tolist())
        game = Wordle(word, rows=ROWS, letters=LETTERS)
        bot = Agent(game)
        while game.is_end() == False:
            if "P" in str(control).upper():
                u_inp = input("\n* PLEASE GUESS A 5 LETTER WORD\n")
            else:
                u_inp = bot.choose_action()
            if game.valid_guess(u_inp) == True:
                game.update_board(u_inp)
                if "P" in str(control).upper():
                    clearConsole()
                    print("* COLORS & GUESSES:")
                    for c, b in zip(game.colours, game.board):
                        colors_string = "".join(c)
                        guess_string = "".join(b)
                        if (
                            guess_string != colors_string
                        ):  # simple hack to not print blank lines: color string is never a legit word. so if both are equal then its an empty line (we haven't played it yet).
                            print(colors_string, guess_string)
            else:
                print("ERROR - WORDS MUST BE 5 LETTERS")
        r = game.game_result()
        if "P" in str(control).upper():
            if r[0] == True:
                if r[1] > 0:
                    print(Fore.GREEN + f"\nCONGRATS YOU WON IN {r[1] + 1} GUESSES!\n" + Style.RESET_ALL)
                else:
                    print(Fore.GREEN + f"\nCONGRATS YOU WON IN {r[1] + 1} GUESS!\n" + Style.RESET_ALL)
            else:
                print(Fore.LIGHTRED_EX + f"\nSORRY YOU DID NOT WIN.\n" + Style.RESET_ALL)
            print(np.array(game.board), "\n")
        results.append({"word": word, "result": r[0], "moves": r[1] + 1})

    results = pd.DataFrame(results)
    print(results)
    print(
        f'Win Percent = {(len(results[results["result"]==True]) / len(results)) * 100}%\nAverage Moves = {results[results["result"]==True]["moves"].mean()}'
    )
elif "A" in str(control).upper():
    clearConsole()
    print(intro())
    print("")
    print(Fore.YELLOW + Style.BRIGHT + "GAME ASSIST ACTIVATED\n---------------------" + Style.RESET_ALL)
    game = Wordle(None, rows=ROWS, letters=LETTERS)
    bot = Agent(game)
    for i in range(ROWS):
        guess = bot.choose_action()
        print(f"\nSuggested Word = {guess}\n")
        u_inp = input(Fore.WHITE + "What were the colours returned [ex. " + Fore.YELLOW + Style.BRIGHT + "y" + Fore.BLACK + Style.BRIGHT + "b" + Fore.GREEN + Style.BRIGHT + "gg" + Fore.YELLOW + Style.BRIGHT + "y" + Style.RESET_ALL + Fore.WHITE + "]?\n" + Style.RESET_ALL)
        if u_inp == "ggggg":
          clearConsole()
          print(intro())
          print("")
          print(Fore.GREEN + Style.BRIGHT + "Congrats you did it!" + Style.RESET_ALL)
          exit(0)
        game.colours[i] = [s for s in str(u_inp).upper()]
        game.board[i] = [s for s in str(guess).upper()]
        game.g_count += 1
        for x, s in enumerate(game.colours[i]):
            if s == "Y":
                if guess[x] in bot.y_letters:
                    bot.y_letters[guess[x]].append(x)
                else:
                    bot.y_letters[guess[x]] = [x]
            elif s == "B":
                if guess[x] in bot.g_letters:
                    bot.g_letters.append(guess[x])
            elif s == "G":
                bot.prediction[x] = guess[x]
