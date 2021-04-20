# 1. Greeting
number_dictionary = {}
print("Welcome to Jeon's calculator")
# 2. Ask and check the vlaidity of first number.
#   2-1. Build a function to check whether the input is valid number or not.
def check_number(initial_number):
    # (Decimal point and minus, plus symbol is removed to check if the input is only numbers.)
    number_to_list = list(initial_number)
    while "." in number_to_list:
        number_to_list.remove(".")
    while "," in number_to_list:
        number_to_list.remove(",")
    while "-" in number_to_list:
        number_to_list.remove("-")
    while "+" in number_to_list:
        number_to_list.remove("+")
    list_to_string = ""
    list_to_string = list_to_string.join(number_to_list)
    return list_to_string.isdigit()


while True:

    #   2-2. Request to input the first number.
    initial_number = input("Please input the first number.\n")

    #   2-3. Check if the number is valid.
    while check_number(initial_number) == False:
        initial_number = input("Please input numbers only\n")
    # 3. Ask and check the validity of operation.
    operation = input("Please pick an operation. (/, *, +, -)\n")
    while operation not in ("/", "*", "+", "-"):
        operation = input(
            "Please pick an operation from the right side. (/, *, +, -)\n"
        )
    initial_number = float(initial_number)

    #   3-1. Add the initial number to the dictionary.
    number_dictionary["initial_number"] = initial_number

    # 4. Ask next number and check its validity.
    next_number = input("Please input next number\n")
    while check_number(next_number) == False:
        next_number = input("Please input numbers only\n")
    next_number = float(next_number)

    #   4-1. Add the next number to the dictionary.
    number_dictionary["next_number"] = next_number

    # 5. Make functions for operation.
    def add(x, y):
        return print(number_dictionary[initial_number] + number_dictionary[next_number])

    def minus(x, y):
        return print(number_dictionary[initial_number] - number_dictionary[next_number])

    def multiply(x, y):
        return print(number_dictionary[initial_number] * number_dictionary[next_number])

    def division(x, y):
        return print(number_dictionary[initial_number] / number_dictionary[next_number])

    if operation == "+":
        add(number_dictionary[initial_number], number_dictionary[next_number])
    elif operation == "-":
        minus(number_dictionary[initial_number], number_dictionary[next_number])
    elif operation == "*":
        multiply(number_dictionary[initial_number], number_dictionary[next_number])
    elif operation == "/":
        division(number_dictionary[initial_number], number_dictionary[next_number])
    # 6. Ask if they want to reset the result of continue with the output.
    reset_or_continue = input("Do you want to continue? Y/N\n")
    #   6-1. Check if the input is valid.
    while reset_or_continue.lower() not in ("y", "yes", "n", "no"):
        reset_or_continue = input(
            "Please type 'Y' if you want to continue or 'N' for reset the result."
        )
    if reset_or_continue.lower() in ("y", "yes"):
        number_dictionary[initial_number] = number_dictionary[next_number]
        print(number_dictionary)
        continue
    elif reset_or_continue.lower() in ("n", "no"):
        break