# Greeting
# Ask if a user wants encode or decode.
#   If a user wants encode,
#       Ask to input a phrase.
#       Ask to type the shift number.
#   If a user wants decode,
#       Ask to input a encoded phrase.
#       Ask to type assigned shift number.
# Ask if a user wants to go to beginning again.

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

        shift_number = input("Please type the shift number\n")
        # Check whether the input is valid number.

    else:
        message = input("Please type your encoded message.")
