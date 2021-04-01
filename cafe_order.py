print("Welcome to Jeon's cafe. Please let me know what you want!")
order_menu = input(
    "Which Beverage do you want?\n--MENU--\n[COFEE]\nLong black:        $ 2.5\nEspresso shot:     $ 2.0\nCaffe latte:       $ 3.0\nCaffe mocha:        $ 4.0\nCaramel macchiato: $ 4.5\n\n[NON-COFEE]\nThai tea latte:    $ 4.5\nCamomile tea:      $ 2.5\nMilk tea:          $ 3.5\n\n[CAKES]\nChocolate cake:    $ 3.0\nStrawberry cake:   $ 3.5\nI would like to have: "
)

bill_count = 0
menu = (
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
)

# When a customer makes typo or uses abbreviation.
# Long black

while not order_menu.lower() in menu:
    order_menu = input(
        "Sorry, I don't understand. Please pick a menu from the menu :)\n"
    )

    if order_menu.lower() in ("long", "black"):
        menu_check = input("Long black right?(Y/N)\n")
        while menu_check.lower() in ("yes", "y"):
            order_menu = "Long black"
            print(f"{order_menu}, okay!")
        while (menu_check.lower() in menu) or (menu_check.lower() in ("no", "n")):
            menu_check = input("Please order from the menu.\n")

    # Caffe latte? or Thai tea latte?
if order_menu.lower() == "latte":
    menu_check = input("Caffe latte? or thai tea latte? (caffe/thai)\n")
    if menu_check.lower() in ("caffe", "caffe latte"):
        order_menu = "Caffe latte"
        print(order_menu, "okay!")
    elif menu_check.lower() in ("thai", "thai tea", "thai tea latte"):
        order_menu = "Thai tea latte"
        print(f"{order_menu}, got it!")
    else:
        order_menu = input("Please select a beverage on the menu.\n")

    # Caffe latte? or caffe mocha?
if order_menu.lower() == "caffe":
    menu_check = input("Caffe latte? or caffe mocha? (latte/mocha)\n")
    if menu_check.lower() in ("caffe latte", "latte", "cafe latte"):
        order_menu = "Caffe latte"
        print(order_menu, "okay!")
    elif menu_check.lower() in ("caffe mocha", "mocha", "cafe mocha"):
        order_menu = "Thai tea latte"
        print(f"{order_menu}, got it!")
    else:
        order_menu = input("Please select a beverage on the menu.\n")

    # Milk tea
if order_menu.lower() == "milk":
    menu_check = input("Hmm, do you mean milk tea? (Y/N)\n")
    if menu_check.lower() in ("yes", "y"):
        order_menu = "Milk tea"
        print(f"{order_menu}, okay!")
    else:
        order_menu = input("Please order from the menu.\n")
    # Chocolate cake? or strawberry cake?
if order_menu.lower() == "cake":
    menu_check = input("Chocolate cake? or strawberry cake? (choco/straw)\n")
    if menu_check.lower() in ("choco", "chocolate", "chocolate cake"):
        order_menu = "Chocolate cake"
        print(order_menu, "okay!")
    elif menu_check.lower() in ("straw", "strawberry", "strawberry cake"):
        order_menu = "strawberry cake"
        print(f"{order_menu}, got it!")
    else:
        order_menu = input("Please select a beverage on the menu.\n")

if order_menu.lower() in ("esp", "espresso"):
    order_menu = "Espresso shot"
    # Caramel macchiato
elif order_menu.lower() in ("caramel", "macchiato"):
    order_menu = "Caramel macchiato"
    print(f"{order_menu}, okay :>")
    # Caffe mocha
elif order_menu.lower() == "mocha":
    order_menu = "Caffe mocha"
    print(f"{order_menu}, okay :)")
    # Thai tea latte
elif order_menu.lower() == "thai":
    order_menu = "Thai tea latte"
    print(f"{order_menu}, got it!")
    # Camomile tea
elif order_menu.lower() == "camomile":
    order_menu = "Camomile tea"
    print(f"{order_menu}, got it!")
    # Chocolate cake
elif order_menu.lower() in ("chocolate", "choco"):
    order_menu = "Chocolate cake"
    print(f"{order_menu}, okayyy")
    # Strawberry cake
elif order_menu.lower() in ("strawberry", "straw"):
    order_menu = "Strawberry cake"
    print(f"{order_menu}, got it!")

print(f"One {order_menu}, anything else?")
