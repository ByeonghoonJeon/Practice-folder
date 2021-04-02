# This programm is for practice of randomisation code.
import random

random_int = random.randint(1, 100)

if random_int in range(1, 11):
    print("top 10")
elif random_int in range(11, 31):
    print("top 30")
elif random_int in range(31, 71):
    print("top 70")
else:
    print(random_int)
