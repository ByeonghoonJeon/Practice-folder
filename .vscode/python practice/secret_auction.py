# 1.  Greeting
print("Welcome to Jeon's blind auction program!")
print(
    "&& Rule: In the blind auction, if there are identical bid with one item, the winner is the first person who input his/her bid!"
)
# 2. Ask name
bid_log_dictionary = {}
#   2-1. Creat function that checks if it is a valid name
def name_check(name):

    name_check = list(name)

    while "." in name_check:
        name_check.remove(".")
    while " " in name_check:
        name_check.remove(" ")

    list_to_string = ""
    list_to_string = list_to_string.join(name_check)
    return list_to_string.isalpha()


while True:
    #   2-2. Ask name
    name = input("Please input your name\n")
    name_check(name)
    #   2-3. Check if the name is valid.
    #       2-3-1. Check if the name is already existed on the dictionary.
    while name in bid_log_dictionary:
        name = input("The name is already used. Please input another name\n")
    #        2-3-2. Check if the name is comprised with Alphabet.
    while name_check(name) != True:
        name = input("Please input Alphabet and period only.\n")

    # 3. Ask bid and add to the dictionary.
    bid = input(f"{name}, what's your bid? \n$ ")
    #   3-1. Convert bid to list and remove "." and "," to check if the bid is valid number.
    bid_check = list(bid)
    while "." in bid_check:
        bid_check.remove(".")
    while "," in bid_check:
        bid_check.remove(",")
    bid_check_to_string = ""
    bid_check_to_string = bid_check_to_string.join(bid_check)

    while bid_check_to_string.isdigit() == False:
        bid = input("Please input your bid with numbers only.\n$ ")

    #   3-3 Add inputs to the dictionry.
    bid_log_dictionary[name] = bid
    # 4. Ask if there is another participant.
    another_participant = input("Are there any other participant? (Y/N)\n")

    #   4-1. Check if the input is valid.
    while another_participant.lower() not in ("yes", "y", "no", "n"):
        another_participant = input("Please input valid answer. (Y/N)\n")

    # 5. If the answer is Y, go to 2-2
    if another_participant.lower() in ("yes", "y"):
        continue
    elif another_participant.lower() in ("no", "n"):
        break

# 6. Determine a bid winner and reveal him/her with bid.
bid_winner = max(bid_log_dictionary)
print(f"The winner is {bid_winner} with $ {bid}!")
