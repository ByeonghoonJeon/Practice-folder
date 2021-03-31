print("Welcome to Byeonghoon's Age Calculator. This program provide your or someone's age at the specific date you are enquiring.")
current_day = int(input("Please input the DAY you want to enquire (DD):\n"))
while current_day < 1 or current_day > 31:
    print("!", current_day, "is not existing date. Please check your date again.")
    current_day = int(input("Please input again for the DAY you want to enquire:\n"))
print(f"Date: {current_day}. Confirmed.")


current_month = int(input("Please input the MONTH you want to enquire (MM):\n"))
while current_month < 1 or current_month > 12:
    print("!", current_month, "is not existing month. Please check your month again.")
    current_month = int(
        input("Please input again for the MONTH you want to enquire (MM):\n")
    )

while ((current_day == 31) and (current_month in (2, 4, 6, 9, 11))) or (
    (current_day == 30) and (current_month == 2)
):
    print(
        "! The date "
        f"{current_day} in the month {current_month} is not exist. Please try again."
    )
    current_day = int(input("Please input the DAY you want to enquire (DD):\n"))
    while current_day < 1 or current_day > 31:
        print("!", current_day, "is not existing date. Please check your date again.")
        current_day = int(
            input("Please input again for the DAY you want to enquire (DD):\n")
        )
    print(f"Date: {current_day}. Confirmed.")

    current_month = int(input("Please input the MONTH you want to enquire (MM):\n"))
    while (current_month < 1) or (current_month > 12):
        print(
            f"! {current_month} is not existing month. Please check your month again."
        )
        current_month = int(
            input("Please input again for the MONTH you want to enquire (MM):\n")
        )
print(f"Date: {current_day}\nMonth: {current_month}. Confirmed.")

current_year = int(input("Please input the YEAR you want to enquire: \n"))
while current_year < 0 or current_year > 9999:
    print("! Please input valid year. (from 0 ~ 9999)!")
    current_year = int(input("Please input the YEAR you want to enquire: \n"))
while (
    (current_day == 29)
    and (current_month == 2)
    and (
        ((current_year % 4) == (1 or 2 or 3))
        or ((current_year % 4) and (current_year % 100) == 0)
        or (((current_year % 4) and (current_year % 100) and (current_year % 400)) > 0)
    )
):
    print(f"! {current_year} does not have 29th day in February.")
    current_year = int(input("Please input the YEAR you want to enquire again: \n"))
print(f"Year: {current_year}. Confirmed.")
print(f"Enquiring Date is: {current_day}. {current_month}. {current_year}.")


birth_day = int(input("Please input your or someone's birth DAY (DD):\n"))
while birth_day < 1 or birth_day > 31:
    print(
        "!",
        birth_day,
        "is not existing date. Please check your or someone's date again.",
    )
    birth_day = int(input("Please input your or someone's birth DAY again:\n"))
print(f"Date of birth: {birth_day}. Confirmed.")


birth_month = int(input("Please input your or someone's birth MONTH (MM):\n"))
while birth_month < 1 or birth_month > 12:
    print(
        "!",
        birth_month,
        "is not existing month. Please check your or someone's month again.",
    )
    birth_month = int(input("Please input your or someone's birth MONTH again (MM):\n"))

while ((birth_day == 31) and (birth_month in (2, 4, 6, 9, 11))) or (
    (birth_day == 30) and (birth_month == 2)
):
    print(
        "! The date "
        f"{birth_day} in the month {birth_month} is not exist. Please try again."
    )
    birth_day = int(input("Please input your or someone's birth DAY (DD):\n"))
    while birth_day < 1 or birth_day > 31:
        print(
            "!",
            birth_day,
            "is not existing date. Please check your or someone's date again.",
        )
        birth_day = int(input("Please input your or someone's birth DAY again (DD):\n"))
    print(f"Date: {birth_day}. Confirmed.")

    birth_month = int(input("Please input your or someone's birth MONTH (MM)\n"))
    while (birth_month < 1) or (birth_month > 12):
        print(
            f"! {birth_month} is not existing month. Please check your or someone's month again."
        )
        birth_month = int(
            input("Please input your or someone's birth MONTH again (MM)\n")
        )
print(f"Date: {birth_day}\nMonth: {birth_month}. Confirmed.")

birth_year = int(input("Please input your or someone's birth YEAR: \n"))
while birth_year < 0 or birth_year > 9999:
    print("! Please input valid year. (from 0 ~ 9999")
    birth_year = int(input("Please input your or someone's birth YEAR agian:\n"))
while (
    (birth_day == 29)
    and (birth_month == 2)
    and (
        ((birth_year % 4) == (1 or 2 or 3))
        or ((birth_year % 4) and (birth_year % 100) == 0)
        or (((birth_year % 4) and (birth_year % 100) and (birth_year % 400)) > 0)
    )
):
    print(f"! {birth_year} does not have 29th day in February.")
    birth_year = int(input("Please input your or someone's birth YEAR again: \n"))
print(f"Year: {birth_year}. Confirmed.")
print(f"Birth Date is: {birth_day}. {birth_month}. {birth_year}.")

result = (
    int(current_year)
    - int(birth_year)
    - 1
    + int(
        (
            current_month > birth_month
            or ((current_month >= birth_month) and (current_day >= birth_day))
        )
        and current_year >= birth_year
    )
)
if result < 0:
    print("Sorry, we can not provide the age before you or someone born")
else:
    print("Your or someone's age at the day you enquired was:", result, "years old")
if (
    (birth_year == current_year)
    and (birth_month == current_month)
    and (birth_day == current_day)
):
    print("It is the day you or someone borned !")
