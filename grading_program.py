# 1. Create students score dictionary.
students_score = {}

# 2. Input students name and score, and check if input is correct. (Alphabet, period, and blank only.)

#   2.1 Creat a function that evaluate the validity of name.
def check_name(name):
    #   2.1.1 Remove period and blank and check it if the name is comprised with only Alphabet.
    #   2.1.1.1 Make a list of spelling in the name.
    list_of_spelling = list(name)
    #   2.1.1.2 Remove period and blank from the list.
    while "." in list_of_spelling:
        list_of_spelling.remove(".")
    while " " in list_of_spelling:
        list_of_spelling.remove(" ")

    #   2.1.1.3 Convert the list to a string.
    list_to_string = ""
    list_to_string = list_to_string.join(list_of_spelling)

    #   2.1.1.4 Return if the string is Alphabet.
    return list_to_string.isalpha()


#   2.2 Input student's name.
name = input("Please input student's name. \n")
check_name(name)
#   2.3 Check if the name is alphabet. If not, ask to input correct name again.
while check_name(name) != True:
    name = input("Please input student's name. (Alphabet and period only.)\n")

score = input(f"Please input {name}'s score.\n")