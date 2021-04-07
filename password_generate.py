import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = [
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
]

symbols = [
    "!",
    "@",
    "#",
    "$",
    "%",
    "^",
    "&",
    "*",
    "(",
    ")",
    "_",
    "-",
    "=",
    "+",
    ">",
    "<",
    "?",
    ";",
    ":",
    ",",
    ".",
    "/",
]

# Greeting and ask how many digit they want for their password.
total_digit = 0
password = ""
print("Welcome to password generator!")
total_digit = input("How many digits would you like to have in your password?\n")
while True:
    # Check if input is digit and valid number (valid: total_digit > 0).
    while not total_digit.isdigit() or int(total_digit) == 0:
        total_digit = input("Please input valid number only.(Greater than zero)\n")

    # Print input
    print("Total", total_digit, "digits, okay!")

    # Ask how many letters do they want for their password.
    number_of_letters = input(
        "How many letters would you like to have in your password?\n"
    )
    # Check if input is digit and valid number (valid: total_digit >= 0)
    while not number_of_letters.isdigit() or int(number_of_letters) < 0:
        number_of_letters = input("Please input valid number only.\n")
    # Count remaining digits and inform them how many digits are needed to be assigned.
    total_digit = int(total_digit) - int(number_of_letters)
    if total_digit == 0:
        break
    print("You can assign maximum", total_digit, "digits more.")

    number_of_numbers = input(
        "How many numbers would you like to have in your password?\n"
    )
    while not number_of_numbers.isdigit():
        number_of_numbers = input("Please input valid number only.\n")
    total_digit -= number_of_numbers
    print("You can assign maximum", total_digit, "digits.")

    number_of_symbals = input(
        "How many symbols would you like to have in your password?\n"
    )
    while not number_of_symbals.isdigit():
        number_of_symbals = input("Pleases input valid number only.\n")
    total_digit -= number_of_symbals

    while total_digit > 0:
        print("Still", total_digit, "digits are not assigned. Please start from first.")
        continue
print("None")
