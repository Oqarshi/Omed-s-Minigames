import time
from colorama import Fore, Style

def printing(text, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def intro():
    return """███ █▄┼▄█ ███ ██▄' ███ ┼┼ █▄┼▄█ ███ █┼┼█ ███ ████ ███ █▄┼▄█ ███ ███.\n█┼█ █┼█┼█ █▄┼ █┼█' █▄▄ ┼┼ █┼█┼█ ┼█┼ ██▄█ ┼█┼ █┼▄▄ █▄█ █┼█┼█ █▄┼ █▄▄▀\n█▄█ █┼┼┼█ █▄▄ ███' ▄▄█ ┼┼ █┼┼┼█ ▄█▄ █┼██ ▄█▄ █▄▄█ █┼█ █┼┼┼█ █▄▄ ▄▄█ ▀"""

print(intro())
print("")

explaination = """ERROR: _*Indevelopment_Game/Tool_Unavailable*_"""

printing(Fore.RED + Style.BRIGHT + explaination + Style.RESET_ALL)