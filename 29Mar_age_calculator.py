current_day = int(input("Please input the DAY you want to enquire (DD):\n"))
while current_day < 1 or current_day > 31:
    print(current_day, "is not existing date. Please check your date again.")
    current_day = int(input("Please input again for the DAY you want to enquire:\n"))
print(f"{current_day}. confirmed")


current_month = int(input("Please input the MONTH you want to enquire (MM)\n"))
while current_month < 1 or current_month > 12:
    print(current_month, "is not existing month. Please check your month again.")
    current_month = int(
        input("Please input again for the MONTH you want to enquire:\n")
    )
print(f"{current_month}. confirmed")

while (current_day == 31) and (current_month in (2, 4, 6, 9, 11)):
    print ("date" f"{current_day}" in "month" {current_month} "is not exist. Please try again.")
    while current_day < 1 or current_day > 31:
        print(current_day, "is not existing date. Please check your date again.")
        current_day = int(input("Please input again for the DAY you want to enquire:\n"))
    print(f"{current_day}. confirmed")
    while current_month < 1 or current_month > 12:
        print(current_month, "is not existing month. Please check your month again.")
        current_month = int(input("Please input again for the MONTH you want to enquire:\n"))
print(f"{current_month}. confirmed")

if current_month not in range(1, 13):
    print(current_month, "is incorrect information. Please check your input again.")
if current_day == 31 and current_month in (2, 4, 6, 9, 11):
    print("Sorry,", current_day, "th day is not exist on ")
current_year = input("Please input the YEAR you want to enquire ")
birth_day = input("Please input your DAY of birth ")
if birth_day not in range(1, 32):
    print(birth_day, "is not existing date. Please check your date again.")
birth_month = input("Please input your MONTH of birth ")
if birth_month not in range(1, 13):
    print(birth_month, " is incorrect information. Please check your input again.")
birth_year = input("Please input your YEAR of birth ")

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
    print("Sorry, we can not provide your age before you born")
else:
    print("Your age at the day you enquired was:", result, "years old")
