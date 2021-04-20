# 1. Greeting

print("Welcome to Jeon's calculator")
# 2. Ask and check the vlaidity of first number.
#   2-1. Build a function to check whether the input is valid number or not.
def check_number(initial_number):
    # (Decimal point is removed to check if the input is only numbers.)
    number_to_list = list(initial_number)
    while "." in number_to_list:
        number_to_list.remove(".")
    while "," in number_to_list:
        number_to_list.remove(",")
    list_to_string = ""
    list_to_string = list_to_string.join(number_to_list)
    return list_to_string.isdigit()


#   2-2. Request to input the first number.
initial_number = input("Please input the first number.\n")

#   2-3. Check if the number is valid.
while check_number(initial_number) == False:
    initial_number = input("Please input numbers only\n")
# 3. Ask operation.
operation = input("Please pick an operation. (/, *, +, -)")
