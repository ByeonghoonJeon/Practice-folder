import random
# Function 1.
# Thousand separator function.
def thousand_separator(number):
    return "{:,}".format(number)


# 1. Greeting
print("Welcome to Jeon's Blackjack.")

# 2. Give $ 1,000 to user. And explain this game's goal.
print("Your seed money is $ 1,000. Reach to the highest balance!")
balance = 1000
thousand_separated_balance = thousand_separator(balance)

print(f"Balance: $ {thousand_separated_balance}")
# 3. Make a dictionary for recording performance of users.

balance_record = {}

# 4. Ask ID and add to the dictionary.
user_id = input("Please input an ID\n")
balance_record[user_id] = balance


# 5. Ask how much user will bet.
betting = input("Betting minimum is $ 100\nYour betting: ")

# 5-1. Check if the input is valid number.
while betting.isdigit() == False or int(betting) > balance or int(betting) <= 0:
    betting = input(
        f"Please bet within your balance.\nYour balance: $ {thousand_separated_balance}\n"
    )
betting = int(betting)
thousand_separated_betting = thousand_separator(betting)
balance -= betting
balance_record[user_id] = balance
print(
    f"Your betting: $ {thousand_separated_betting}\nYour balance: $ {balance_record[user_id]}"
)

# 6. Make a card dictionary.
card_symbol_list = ["Spades","Clubs","Diamonds","Hearts"]
number_list = ["A","2","3","4","5","6","7","8","9","J","Q","K"]
random_card_symbol = random.choice(card_symbol_list)
random_number = random.choice(number_list)
player_first_card = [random_card_symbol, random_number]
player_second_card = [random_card_symbol, random_number]
while player_first_card == player_second_card:
    player_first_card = [random_card_symbol, random_number]
    player_second_card = [random_card_symbol, random_number]

print (player_first_card)
