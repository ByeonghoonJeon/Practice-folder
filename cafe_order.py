# [1] Greeting.
# [2] Ask for menu choice, exhibit the menu.
#   [2-1] If input is in menu,
#       [2-1-1] Accept order.
#       [2-1-2] Count bill.
#       [2-1-3] Ask quantity.
#           [2-1-3-1] Check if quantity is digit.
#               [2-1-3-1-1] If quantity is digit,
#                   [2-1-3-1-1-1] Accept order.
#                   [2-1-3-1-1-2] Count bill.
#                   [2-1-3-1-1-3] Check if the order is a beverage,
#                       [2-1-3-1-1-3-1] If a beverage, ask size choice with informing extra fee for the tall size. (Regular and tall size(+ $ 0.5))
#                           [2-1-3-1-1-3-1-1] If input properly, count bill.
#                           [2-1-3-1-1-3-1-2] If input is invalid code, go to [2-1-3-1-1-3-1].
#                       [2-1-3-1-1-3-2] If the order is not a beverage, go to [2-1-3-1-1-4].
#                    [2-1-3-1-1-4] Ask if a customer wants other menu as well. (Y/N)
#                        [2-1-3-1-1-4-1] If Y, go to [2]
#                        [2-1-3-1-1-4-2] If N, go to [Final]
#                        [2-1-3-1-1-4-3] If invalid code, go to [2-1-3-1-1-4] requesting valid code.
#                    [2-1-3-1-2] If quantity is not digit, go to [2-1-3-1] requesting valid code.

#   [2-2] If input is partially match to the menu,
#       [2-2-1] Request confirmation. (Y/N)
#           [2-2-1-1] Check if valid answer.
#               [2-2-1-1-1] If valid, go to [2-1-1]
#               [2-2-1-1-2] If invalid, go to [2-2-1] requesting valid code.

#   [2-3] If input does not exist in the menu, go to [2] requesting valid menu.

# [Final] Print total bill and say goodbye.
###########################################################################################################################

# Variations for total bill
bev_bill = 0
size_bill = 0

# Expected input for orders from customers.

menu = [
    "long black",
    "long",
    "black",
    "espresso shot",
    "espresso",
    "esp",
    "caffe latte",
    "caffe",
    "latte",
    "caffe mocha",
    "mocha" "caramel macchiato",
    "caramel",
    "macchiato",
    "thai tea latte",
    "thai",
    "camomile tea",
    "camomile",
    "milk tea",
    "milk",
    "chocolate cake",
    "chocolate",
    "cake",
    "strawberry cake",
    "strawberry",
]

# Greeting

print("Welcome to Jeon's cafe. Please let me know what you want!")

# The first menu exhibition and the menu will be repeated until customer input a valid code(expected order, above).

while True:
    order_menu = input(
        "Which Beverage do you want?\n--MENU--\n[COFEE]\nLong black:        $ 2.5\nEspresso shot:     $ 2.0\nCaffe latte:       $ 3.0\nCaffe mocha:       $ 4.0\nCaramel macchiato: $ 4.5\n\n[NON-COFEE]\nThai tea latte:    $ 4.5\nCamomile tea:      $ 2.5\nMilk tea:          $ 3.5\n\n[CAKES]\nChocolate cake:    $ 3.0\nStrawberry cake:   $ 3.5\nI would like to have: "
    )
    # If a customer orders "long black with the full name, count bill and ask quantity"
    if order_menu.replace(" ", "", 1).lower() == "longblack":
        order_menu = "Long black"
        bev_bill += 2.5
        order_quantity = input(f"How many {order_menu} do you want?\n")

        # Check if quantity is digit. If not, recommend to input number only.
        while not order_quantity.isdigit():
            order_quantity = input("Please input valid numbers only.\n")

        # If quantity is digit, add to a bill and print order acceptance ment.
        if order_quantity.isdigit():
            print(order_quantity, order_menu, "got it!")
        bev_bill *= int(order_quantity)
        break

    elif order_menu.lower() == ("long") or order_menu.lower() == ("black"):
        check_menu = input("Do you mean Long black? (Y/N)\n")
        while not check_menu.lower() in ("y", "yes"):
            check_menu = input("Please type Y/N only.\n")
        if check_menu.lower() in ("y", "yes"):
            order_menu = "Long black"
            bev_bill += 2.5
        order_quantity = input(f"How many {order_menu} do you want?\n")

        while not order_quantity.isdigit:
            order_quantity = input("Please input numbers only.")
            break
        bev_bill = bev_bill * int(order_quantity)
        print(order_quantity, order_menu, "got it!")
        break

    else:
        print("Sorry, I don't understand. Please refer to the menu again.")
        continue


def total_bill():
    return bev_bill + exta_bill


print("Total bill is USD", total_bill())

# if order_menu.replace(" ", "", 1) in menu:
#     if order_menu.replace(" ", "", 1).lower() == "longblack":
#         order_menu = "Long black"
#         bill += 2.5
#     while order_menu.lower() in (
#         "long",
#         "black",
#     ):
#         check_menu = input("Do you mean Long black? (Y/N)\n")
#         if check_menu.lower() in ("y", "yes"):
#             order_menu = "Long black"
#             print(f"{order_menu}, okay!")
#             bill += 2.5
#         elif check_menu.lower() in ("n", "no"):
#             order_menu = input("Please select your menu from above :)\n")
#         else:
#             order_menu = input(
#                 "I am so sorry, I don't understand. Please check the menu above :(\n"
#             )

#     if order_menu.replace(" ", "", 1).lower() == "espressoshot":
#         order_menu = "Espresso shot"
#         bill += 2.0
#     while order_menu.lower() in ("espresso", "esp"):
#         check_menu = input("Do you mean Espresso shot? (Y/N)\n")
#         if check_menu.lower() in ("y", "yes"):
#             order_menu = "Espresso shot"
#             bill += 2.0
#         elif check_menu.lower() in ("no", "n"):
#             order_menu = input("Please select your menu from above :)\n")
#         else:
#             order_menu = input(
#                 "I am so sorry, I don't understand. Please check the menu above :(\n"
#             )
#     if order_menu.replace(" ", "", 1).lower() == "caffelatte":
#         order_menu = "Caffe latte"
#         bill += 3.0
#     while order_menu.lower() in ("latte"):
#         check_menu = input("Do you mean Espresso shot? (Y/N)\n")
#         if check_menu.lower() in ("y", "yes"):
#             order_menu = "Caffe latte"
#             bill += 3.0
#         elif check_menu.lower() in ("no", "n"):
#             order_menu = input("Please select your menu from above :)\n")
#         else:
#             order_menu = input(
#                 "I am so sorry, I don't understand. Please check the menu above :(\n"
#             )
# print(f"One {order_menu}, anything else?")
