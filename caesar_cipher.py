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
print(letters)

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
        while not message.isalnum():
            message = input("Please type letters and numbers only.")
        print("Message received.")

        shift_number = input("Please type the shift number. (1 ~ 61)\n")
        # Check whether the input is valid number.
        while (
            not shift_number.isdigit()
            or int(shift_number) < 1
            or int(shift_number) > 61
        ):
            shift_number = input("Please type the shift number. (1 ~ 61)\n")
        shift_number = int(shift_number)
        for i in range(0, 3):
            print("Encoding." + "." * i)
            sleep(0.3)

        def encode_letter(message, shift_number):
            encoded_message = ""
            for letter in message:
                original_position = letters.index(letter)

                if int(original_position) + int(shift_number) > 61:
                    encoded_position = original_position + (shift_number - 62)
                else:
                    encoded_position = original_position + shift_number

                encoded_letter = letters[int(encoded_position)]
                encoded_message += encoded_letter
            return print(f"Encoded message is: [{encoded_message}]")

        encode_letter(message, shift_number)

        # Encode starts from here.

    else:
        message = input("Please type your encoded message.\n")
        while message not in letters:
            message = input("Please type letters and numbers only.")
        print("Encoded message received.")
        shift_number = input("Please type the shift number.\n")
        # Check whether the input is valid number.
        acceptable_number_range = []
        for a_number in range(1, 62):
            acceptable_number_range.append(a_number)

        acceptable_number_range = str(acceptable_number_range)
        while (shift_number) not in acceptable_number_range:
            shift_number = input("Please type the shift number. (1 ~ 61)\n")

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
