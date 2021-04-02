bill = 0
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
print("Welcome to Jeon's cafe. Please let me know what you want!")

while True:
    order_menu = input(
        "Which Beverage do you want?\n--MENU--\n[COFEE]\nLong black:        $ 2.5\nEspresso shot:     $ 2.0\nCaffe latte:       $ 3.0\nCaffe mocha:       $ 4.0\nCaramel macchiato: $ 4.5\n\n[NON-COFEE]\nThai tea latte:    $ 4.5\nCamomile tea:      $ 2.5\nMilk tea:          $ 3.5\n\n[CAKES]\nChocolate cake:    $ 3.0\nStrawberry cake:   $ 3.5\nI would like to have: "
    )
    if order_menu.replace(" ", "", 1).lower() == "longblack":
        order_menu = "Long black"
        bill += 2.5
        print(f"One {order_menu}, anything else?")
        break

    elif order_menu.lower() == ("long") or order_menu.lower() == ("black"):
        check_menu = input("Do you mean Long black? (Y/N)\n")
        if check_menu.lower() in ("y", "yes"):
            order_menu = "Long black"
            bill += 2.5
            print(f"One {order_menu}, anything else?")
            break

    else:
        print("Sorry, I don't understand. Please refer to the menu again.")
        continue
print(bill)

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
