# This programm is for practice of randomisation code.
import random

print("Welcome to lotto predictor!")

# Ask number range.
number_range = input("Please the largest number in your country's lotto system.\n")

# Check if input is number.

while not number_range.isdigit():
    number_range = input("Please input number only\n")

# Ask how many picks user wants

picks = input("How many picks do you want?\n")

# Check if input is number.

while not number_range.isdigit():
    picks = input("Please input number only\n")

# Randomise 6 numbers.

random_int1 = random.randint(1, int(number_range))
random_int2 = random.randint(1, int(number_range))
random_int3 = random.randint(1, int(number_range))
random_int4 = random.randint(1, int(number_range))
random_int5 = random.randint(1, int(number_range))
random_int6 = random.randint(1, int(number_range))

# Avoid duplicated numbers among 6 numbers above.

for i in range(0, int(picks)):
    random_int1 = random.randint(1, int(number_range))
    random_int2 = random.randint(1, int(number_range))
    random_int3 = random.randint(1, int(number_range))
    random_int4 = random.randint(1, int(number_range))
    random_int5 = random.randint(1, int(number_range))
    random_int6 = random.randint(1, int(number_range))
    while (
        (random_int1 == random_int2)
        or (random_int1 == random_int3)
        or (random_int1 == random_int4)
        or (random_int1 == random_int5)
        or (random_int1 == random_int6)
        or (random_int2 == random_int3)
        or (random_int2 == random_int4)
        or (random_int2 == random_int5)
        or (random_int2 == random_int6)
        or (random_int3 == random_int4)
        or (random_int3 == random_int5)
        or (random_int3 == random_int6)
        or (random_int4 == random_int5)
        or (random_int4 == random_int6)
        or (random_int5 == random_int6)
    ):
        random_int1 = random.randint(1, int(number_range))
        random_int2 = random.randint(1, int(number_range))
        random_int3 = random.randint(1, int(number_range))
        random_int4 = random.randint(1, int(number_range))
        random_int5 = random.randint(1, int(number_range))
        random_int6 = random.randint(1, int(number_range))
    print(random_int1, random_int2, random_int3, random_int4, random_int5, random_int6)
# Print result.

print("Good Luck!")

# I will learn set function to simplify codes.
# I will learn how to organize numbers in order.
