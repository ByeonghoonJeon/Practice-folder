# Greeting
# Ask if a user wants encode or decode.
#   If a user wants encode,
#       Ask to input a phrase.
#       Ask to type the shift number.
#   If a user wants decode,
#       Ask to input a encoded phrase.
#       Ask to type assigned shift number.
# Ask if a user wants to go to beginning again.
from time import sleep
import string

letters = list(string.ascii_letters)
numbers = list(string.digits)
letters += numbers


print("Welcome to Jeon's encoding program.")
while True:
    encode_or_decode = input(
        "Please type 'encode' to encrypt, or 'decode' to decrypt.\n"
    )
    # Check whether the input is valid answer.
    expected_input = ["encode", "decode"]
    while encode_or_decode.lower() not in expected_input:
        encode_or_decode = input(
            "Please type 'encode' to encrypt, or 'decode' to decrypt.\n"
        )
    if encode_or_decode.lower() == "encode":
        message = input("Please type your message.\n")
        print("Message received.")

        shift_number = input("Please type the shift number.\n")
        # Check whether the input is valid number.
        acceptable_number_range = []
        for a_number in range(1, 101):
            acceptable_number_range.append(a_number)

        acceptable_number_range = str(acceptable_number_range)
        while (shift_number) not in acceptable_number_range:
            shift_number = input("Please type the shift number. (1 ~ 100)\n")

        for i in range(0, 3):
            print("Encoding." + "." * i)
            sleep(0.3)

        # Encode starts from here.

    else:
        message = input("Please type your encoded message.\n")
        print("Encoded message received.")
        shift_number = input("Please type the shift number.\n")
        # Check whether the input is valid number.
        acceptable_number_range = []
        for a_number in range(1, 101):
            acceptable_number_range.append(a_number)

        acceptable_number_range = str(acceptable_number_range)
        while (shift_number) not in acceptable_number_range:
            shift_number = input("Please type the shift number. (1 ~ 100)\n")

        for i in range(0, 3):
            print("Decoding." + "." * i)
            sleep(0.3)

    # Check if the user wants to go again or not.
    repeat = input("Please type 'yes' if you want to go again. Otherwise, type 'no'.\n")
    while repeat.lower() not in ("yes", "no"):
        repeat = input(
            "Please type 'yes' if you want to go again. Otherwise, type 'no'.\n"
        )
    if repeat.lower() == "yes":
        continue
    else:
        break
print("Good bye!")
