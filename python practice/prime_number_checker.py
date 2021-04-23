print("Welcome to Jeon's prime number checker.")
input_number = input("Please input a number to figure out if it is a prime number.\n")
while not input_number.isdigit():
    input_number = input("Please input a valid number only. (Greater than zero)\n")


def prime_or_not(input_number):
    input_number = int(input_number)
    number_list = []
    for numbers in range(1, input_number + 1):
        if input_number % numbers == 0:
            number_list.append(numbers)
    if number_list == [1, input_number]:
        print(f"{input_number} is a prime number.")
    else:
        print(f"{input_number} is NOT a prime number.")
    return print(input_number, "can be divided by", number_list)


prime_or_not(input_number)
