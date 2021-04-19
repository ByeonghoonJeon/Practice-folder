# 1. Create students score dictionary.
students_score = {}

# 2. Input students name and score, and check if input is correct. (Alphabet, period, and blank only.)

#   2.1 Creat a function that evaluate the validity of name.
def check_name(name):
    #   2.1.1 Replace period and blank in the name to "" and check it if the name is comprised with only Alphabet.
    name.replace(".", "")
    name.replace(" ", "")
    return name.isalpha()


name = input("Please input student's name. \n")
check_name(name)
while check_name(name) == False:
    name = input("Please input student's name. (Alphabet and period only.)\n")
#   2.2 Name input


student_score = input(f"Please input {name}'s score.")
