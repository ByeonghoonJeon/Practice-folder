# 1. Create students score dictionary.
students_score = {}

# 2. Input students name and score, and check if input is correct. (Alphabet, period, and blank only.)

#   2.1 Creat a function that evaluate the validity of name.
def check_name(name):
    #   2.1.1 Split all the words to evaluate if those are all acceptable characters. (Alphabet, period, and blank.)
    split_name_into_letters = list(name)
    #   2.1.2 Replace "." and " " to a random alphabet
    for i in range(len(split_name_into_letters)):
        if split_name_into_letters[i] == ".":
            split_name_into_letters[i] = "a"
        if split_name_into_letters[i] == " ":
            split_name_into_letters[i] = "a"
        #   2.1.3 If input name is comprised with Alphabet, return "valid"
        for i in range(len(split_name_into_letters)):
            if split_name_into_letters[i].isalpha == True:
                return "valid"


#   2.2 Name input
name = input("Please input student's name. \n")
#   2.3 Evaluation of name
while check_name(name) != "valid":
    name = input("Please input student's name. (Alphabet and period only)\n")
    check_name(name)
print(f"Student name: {name}")
student_score = input("Please input student's score.")
