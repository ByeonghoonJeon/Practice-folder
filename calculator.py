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

    # 4. Ask second number and check its validity.
    second_number = input("Please input next number\n")
    while check_number(second_number) == False:
        second_number = input("Please input numbers only\n")
    calc_result = initial_number, operation, second_number
    print(calc_result)
