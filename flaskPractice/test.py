def divide(numerator, denominator):
    return numerator / denominator

#named parameter
answer = divide(denominator=6, numerator=12)
# print (answer)

# *args (for list )
def add_all_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

answer = add_all_numbers(1, 2, 3, 4, 5)


# **kwargs  (for dictionary)

def print_user_attributes(**kwargs):
    for key, value in kwargs.items():
        print(key + ": "+str(value))

print_user_attributes(
    first_name='Nathan',
    last_name='Jeon',
    age = 30
)

