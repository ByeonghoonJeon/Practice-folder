import random

import string

letters = list(string.ascii_letters)
numbers = list(string.digits)
symbols = list(string.punctuation)

# Greeting and ask how many digit they want for their password.
print("Welcome to password generator!")

# Check if input is digit and valid number (valid: total_digit > 0).
total_digit = input("How many digits would you like to have in your password?\n")
# Intend ZeroDivisionError when the input is zero.
while True:
    try:
        1 / int(total_digit)
        print(f"Total [{total_digit}] digits, okay!")
    # Exceptions for strings and zero inputs.
    except (ValueError, ZeroDivisionError):
        while total_digit == "0" or (not total_digit.isdigit()):
            total_digit = input("Please input valid number only.(Greater than zero)\n")
        print(f"Total [{total_digit}] digits, okay!")

    # Ask how many letters do they want for their password.
    number_of_letters = input(
        f"How many letters would you like to have in your password? (Not more than [{total_digit}] digits.)\n"
    )

    # Check if input is digit and valid number (valid: total_digit >= 0)
    # Check if number of letters exceed total digit.
    try:
        while int(total_digit) < int(number_of_letters):
            number_of_letters = input("Please input valid numbers only.\n")
    except (ValueError):
        while not number_of_letters.isdigit():
            number_of_letters = input("Please input valid numbers only.\n")

    print(f"Total [{number_of_letters}] letters, okay")

    # Count left total digits and,
    # if all the digits are assigned, break.
    total_digit = int(total_digit) - int(number_of_letters)
    if int(total_digit) == 0:
        break
    # Inform user how many digits can be assigned.
    else:
        print(f"! You can assign maximum [{total_digit}] digits more.")

    # Ask how many numbers want to include in the password.
    number_of_numbers = input(
        f"How many numbers would you like to have in your password? (Not more than [{total_digit}] digits.)\n"
    )
    # Check if the input is digit and exceeds total digit.
    try:
        while int(total_digit) < int(number_of_numbers):
            number_of_numbers = input("Please input valid numbers only.\n")
    except (ValueError):
        while not number_of_numbers.isdigit():
            number_of_numbers = input("Please input valid numbers only.\n")

    print(f"Total [{number_of_numbers}] letters, okay")

    # Count left total digit and,
    # if all the digits are assigned, break.
    total_digit = int(total_digit) - int(number_of_numbers)
    if int(total_digit) == 0:
        break
    # If there is still remaining digits, assign it as number of symbol and kindly inform to user.
    else:
        print(
            f"! The rest of [{total_digit}] digits will be automatically assigned as number of symbols."
        )
        break

password_list = []
for i in range(1, int(number_of_letters) + 1):
    password_list += random.choice(letters)
for i in range(1, int(number_of_numbers) + 1):
    password_list += random.choice(numbers)
for i in range(1, int(total_digit) + 1):
    password_list += random.choice(symbols)

random.shuffle(password_list)

password = ""
for i in password_list:
    password += i
print(f"Your password is same as following below.'\n{password}")
