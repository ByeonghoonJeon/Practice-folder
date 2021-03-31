import datetime

current = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
print(
    "Hello, This is BMI calculator that analyses your obesity based on your weight and height.\nThis program requires your body weight and height.\nIf you agree to provide your bio information, please type 'Y'.\nIf you don't agree, then please type 'N' and then program will no longer run."
)
agreement = str(input("# Do you agree to provide your body weight and height? (Y/N)\n"))

while (
    agreement != "Y"
    and agreement != "y"
    and agreement != "YES"
    and agreement != "Yes"
    and agreement != "yes"
    and agreement != "Agree"
    and agreement != "AGREE"
    and agreement != "agree"
    and agreement != "N"
    and agreement != "n"
    and agreement != "NO"
    and agreement != "No"
    and agreement != "no"
    and agreement != "Disagree"
    and agreement != "DISAGREE"
    and agreement != "disagree"
):
    agreement = input("Please input valid code (Y/N)\n")

if (
    agreement == "Y"
    or agreement == "y"
    or agreement == "YES"
    or agreement == "Yes"
    or agreement == "yes"
    or agreement == "Agree"
    or agreement == "AGREE"
    or agreement == "agree"
):

    print(f"[You agreed to provide your bio information at {current}]")
    system_preference = input(
        "If you prefer yard-pound system, please type 'Y'\nfor metric system,please type 'M'\n"
    )
    while (
        system_preference != "Y"
        and system_preference != "y"
        and system_preference != "M"
        and system_preference != "m"
    ):
        system_preference = input("Please input valid code (Y/M)\n")
    if system_preference == "Y" or system_preference == "y":
        print("Yard-pound system confirmed")
        weight = input("Please input your body weight (lb)\n")
        # check if weight is a float
        while not weight.replace(".", "", 1).isdigit():
            # if not, while loop on input until weight is a float
            weight = input("Please input your body weight (lb)\n")
        print(f"Weight: {weight} lb, confirmed")
    elif system_preference == "M" or system_preference == "m":
        print("Metric system confirmed")

elif (
    agreement == "N"
    or agreement == "n"
    or agreement == "NO"
    or agreement == "No"
    or agreement == "no"
    or agreement == "Disagree"
    or agreement == "DISAGREE"
    or agreement == "disagree"
):
    print(
        "You disagreed to provide your bio information. Program will be not operated."
    )
