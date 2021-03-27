current_day = input("Please input the DAY you want to enquire ")
current_month = input("Please input the MONTH you want to enquire ")
current_year = input("Please input the YEAR you want to enquire ")
birth_day = input("Please input your DAY of birth ")
birth_month = input("Please input your MONTH of birth ")
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
