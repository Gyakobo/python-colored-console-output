# Python Colored Console Output

![image](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![image](https://img.shields.io/badge/windows%20terminal-4D4D4D?style=for-the-badge&logo=windows%20terminal&logoColor=white)

Author: [Andrew Gyakobo](https://github.com/Gyakobo)

## Intro

In Python, you can change the color of the text printed to the console by using ANSI escape sequences. These are special codes that can change the color and style of the terminal text.

## Methodology

Here is a simple example:

```python
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
```

Here's a breakdown of the escape sequences:

* `\033[`: This is the escape character and the beginning of the ANSI code.
* `31m, 32m, 33m, etc.`: These are the codes for different colors.
* `0m`: This resets the text color to the default.

The colors available with these codes are:

* 30: Black
* 31: Red
* 32: Green
* 33: Yellow
* 34: Blue
* 35: Magenta
* 36: Cyan
* 37: White

You can also use libraries like colorama to make it easier to work with colored text, especially if you are writing cross-platform applications. Here's an example using colorama:

```python
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
```
`colorama` handles the reset for you, making it a bit easier to manage. To install `colorama`, you can use pip:

```shell
$ pip install colorama
```

## License
MIT
