# 1. Create students score dictionary.
students_score = {}

# 2. Input students name and score, and check if input is correct. (Letters and punctuation only.)

#   2.1 Name validity checking function.
def check_name(name):
    split_name = name.split()
    for i in split_name:
        if i.isalpha() == True:
            return "valid"


# 2.2 Name input
name = input("Please input student's name. \n")
while check_name(name) != "valid":
    name = input("Please input student's name. (Alphabet and period only)\n")
