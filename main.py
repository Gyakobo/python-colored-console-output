# METHOD 1

# ANSI escape sequences for text colors
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
RESET = "\033[0m"

# Printing text in different colors
print(RED + "This is red text" + RESET)
print(GREEN + "This is green text" + RESET)
print(YELLOW + "This is yellow text" + RESET)
print(BLUE + "This is blue text" + RESET)
print(MAGENTA + "This is magenta text" + RESET)
print(CYAN + "This is cyan text" + RESET)

# METHOD 2

from colorama import Fore, Style, init

# Initialize colorama
init()

# Printing text in different colors
print(Fore.RED + "This is red text" + Style.RESET_ALL)
print(Fore.GREEN + "This is green text" + Style.RESET_ALL)
print(Fore.YELLOW + "This is yellow text" + Style.RESET_ALL)
print(Fore.BLUE + "This is blue text" + Style.RESET_ALL)
print(Fore.MAGENTA + "This is magenta text" + Style.RESET_ALL)
print(Fore.CYAN + "This is cyan text" + Style.RESET_ALL)
