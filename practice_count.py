# Count function practice.

print("Welcome, we will let you know about love level with you and (him/her)")

your_name = input("Please type your name.\n")
lover_name = input("Please type his/her name.\n")

# Make lower case for each input

your_name = your_name.lower()
lover_name = lover_name.lower()

# Count how many of alphabet (T, R, U, E) is in your_name and lover_name.

t = your_name.count("t")
r = your_name.count("r")
u = your_name.count("u")
e1 = your_name.count("e")
result1 = t + r + u + e1

l = lover_name.count("l")
o = lover_name.count("o")
v = lover_name.count("v")
e2 = lover_name.count("e")
result2 = l + o + v + e2

# Writing the formula of love level.
lovelevel = result1 * 10 + result2

# Print love level
print("The love level between you and him/her is ", end="")
print(lovelevel)

# Print additional comment.
