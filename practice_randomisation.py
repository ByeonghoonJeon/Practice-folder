# This programm is for practice of randomisation code.
import random

print("Welcome to lotto predictor!")

# Ask number range.
number_range = input("Please the largest number in your country's lotto system.\n")

# Check if input is number.

while not number_range.isdigit():
    number_range = input("Please input number only\n")

# Randomise 6 numbers.

random_int1 = random.randint(1, int(number_range))
random_int2 = random.randint(1, int(number_range))
random_int3 = random.randint(1, int(number_range))
random_int4 = random.randint(1, int(number_range))
random_int5 = random.randint(1, int(number_range))
random_int6 = random.randint(1, int(number_range))

# Avoid duplicated numbers among 6 numbers above.

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

# Print result.

print(random_int1, random_int2, random_int3, random_int4, random_int5, random_int6)
print("Good Luck!")
