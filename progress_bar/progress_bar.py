import random
import time
from colorama import Fore, Style

def run_progress_bar():

    total_steps = 100

    duration = 10

    update_interval = duration / total_steps

    current_progress = 0

    for i in range(total_steps):

        increment = random.randint(1, 10)

        current_progress += increment

        if current_progress > 100:
            current_progress = 100

        percentage = int(current_progress)

        if percentage < 50:
            color = Fore.RED
        elif percentage < 75:
            color = Fore.YELLOW
        else:
            color = Fore.GREEN

        print("{}[{}{}] {}%{}".format(color, "=" * int(current_progress / 5), " " * (20 - int(current_progress / 5)), percentage, Style.RESET_ALL), end="\r")

        if current_progress == 100:
            break

        time.sleep(update_interval)

    print("{}[{}{}] {}%{}".format(Fore.LIGHTYELLOW_EX, "=" * 20, " " * 0, 100, Style.RESET_ALL))

run_progress_bar()