print("Hello, This is a factorial calculator")
number = int(input("Please input a number for factorial calculation:\n"))
print(f"The factorial value of '{number}' is:")
for i in range(number - 1, 1, -1):
    number = number * i
print(number)
