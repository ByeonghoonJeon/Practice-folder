import random
from time import sleep
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

# 3. Ask ID.
user_id = input("Please input an ID\n")



# 4. Make a dictionary for recording performance of users and add player's current balance.
balance_record = {}
balance_record[user_id] = balance

while True:
    # 5. Ask how much user will bet.
    if balance == 0:
        print ("Balance is not enough. Time to go home!")
        break
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

    # 6. Make a card lists.
    number_list = ["A","2","3","4","5","6","7","8","9","J","Q","K"]
    symbol_list = ["♠","♣","♦","♥"]

    # 7. Make an empty dictionary to store picked cards.
    revealed_cards = {}

    # 8. Pick player's first card.
    random_number = random.choice(number_list)
    random_symbol = random.choice(symbol_list)
    player_first_card = random_symbol, random_number
    revealed_cards[random_symbol]=random_number

    # 9. Pick player's second card.
    random_number = random.choice(number_list)
    random_symbol = random.choice(symbol_list)
    player_second_card = random_symbol, random_number


    # 10. If player's second card is already existed in the revealed card dictionary, differentiate it.
    while player_second_card in revealed_cards:
        random_number = random.choice(number_list)
        random_symbol = random.choice(symbol_list)
        player_second_card = random_symbol, random_number
    revealed_cards[random_symbol]=random_number

    # 11. Exhibit player's card pair.
    player_card_pair = player_first_card, player_second_card
    print ("Player's cards:", (player_card_pair))

    # 12. Pick dealer's first card.
    random_number = random.choice(number_list)
    random_symbol = random.choice(symbol_list)
    dealer_first_card = random_symbol, random_number

    # 13. If dealer's first card is in the revealed card dictionary, differentiate it.
    while dealer_first_card in revealed_cards:
        random_number = random.choice(number_list)
        random_symbol = random.choice(symbol_list)
        dealer_first_card = random_symbol, random_number
    revealed_cards[random_symbol]=random_number

    # 14. Pick dealer's second card.
    random_number = random.choice(number_list)
    random_symbol = random.choice(symbol_list)
    dealer_second_card = random_symbol, random_number

    # 15. If dealer's second card is in the revealed card dictionary, differentiate it.
    while dealer_second_card in revealed_cards:
        random_number = random.choice(number_list)
        random_symbol = random.choice(symbol_list)
        dealer_second_card = random_symbol, random_number
    revealed_cards[random_symbol]=random_number

    # 16. Show dealer's first card.
    print (f"Dealer's cards: {dealer_first_card}, (Hidden card)")
    # 17. If dealer's first card is Ace, King, Queen, or Jack, check if dealer's card is black jack.
    if dealer_first_card[1] in ("A", "K", "Q", "J"):
        print (f"Oh! is dealer Black Jack?")
        for i in range(0, 3):
            print("Dealer is checking his cards." + "." * i)
            sleep(1.0)
        if dealer_second_card[1] in ("A")
            print("Dealer is Black Jack!")
            continue
        else: print ("Dealer is not Black Jack.")


print ("See you later!")




