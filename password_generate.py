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
print("Welcome to password generator!")

# Check if input is digit and valid number (valid: total_digit > 0).
total_digit = input("How many digits would you like to have in your password?\n")
# Intend ZeroDivisionError when the input is zero.
while True:
    try:
        1 / int(total_digit)

    # Exceptions for strings and zero inputs.
    except (ValueError, ZeroDivisionError):
        while total_digit == "0" or (not total_digit.isdigit()):
            total_digit = input("Please input valid number only.(Greater than zero)\n")
        print("Total [", total_digit, "] digits, okay!")
    # Print input.
    else:
        print("Total [", total_digit, "] digits, okay!")

    # Ask how many letters do they want for their password.
    number_of_letters = input(
        f"How many letters would you like to have in your password? (Not more than [{total_digit}] digits.)\n"
    )

    # Check if input is digit and valid number (valid: total_digit >= 0)
    # Check if number of letters exceed total digit.
    try:
        int(number_of_letters)
    except (ValueError):
        while not number_of_letters.isdigit():
            number_of_letters = input("Please input valid numbers only.\n")
    else:
        while not number_of_letters.isdigit() and (
            int(total_digit) < int(number_of_letters)
        ):
            number_of_letters = input("Please input valid numbers only.\n")
    print("Total [", number_of_letters, "] letters, okay")

    # If all the digits are assigned, break
    if int(total_digit) == int(number_of_letters):
        break

    # Count remaining digits and inform them how many digits are needed to be assigned.
    total_digit = int(total_digit) - int(number_of_letters)
    if total_digit == 0:

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

print("Your password is,")
