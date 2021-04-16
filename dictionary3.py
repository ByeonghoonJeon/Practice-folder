# Dictionary practive with EDX course.

# Recall in the previous problem you counted the number of
# instances of a certain first name in a list of full names.
# You returned a dictionary with the name as the key, and the
# number of times it appeared as the value.
#
# Modify that code such that instead of having a count as the
# value, you instead have a list of the full names that had
# that first name. So, each key in the dictionary would still
# be a first name, but the values would be lists of names.
# Make sure to sort the list of names, too.
#
# Name this new function name_lists.


# Add your function here!
def name_lists(name_list):
    splited_name_list = []
    first_name_dictionary = {}
    last_name_list = []
    for names in name_list:
        splited_name_list.append(names.split())

    print(splited_name_list)
    for i in range(0, len(splited_name_list)):
        first_name = splited_name_list[i][0]
        last_name = splited_name_list[i][1]
        if first_name not in first_name_dictionary:
            last_name_list = last_name
            first_name_dictionary[first_name] = last_name
        elif first_name in first_name_dictionary:
            last_name_list.append(last_name)
            first_name_dictionary[first_name] += last_name

    return first_name_dictionary


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print (although the order of the keys may vary):
# {'Shelba': ['Shelba Barthel', 'Shelba Crowley', 'Shelba Fernald', 'Shelba Fry', 'Shelba Odle'],
#'David': ['David Joyner', 'David Zuber'], 'Brenton': ['Brenton Joyner', 'Brenton Zuber'],
#'Maren': ['Maren Fry'], 'Nicol': ['Nicol Barthel']}

name_list = [
    "David Joyner",
    "David Zuber",
    "Brenton Joyner",
    "Brenton Zuber",
    "Nicol Barthel",
    "Shelba Barthel",
    "Shelba Crowley",
    "Shelba Fernald",
    "Shelba Odle",
    "Shelba Fry",
    "Maren Fry",
]
print(name_lists(name_list))
