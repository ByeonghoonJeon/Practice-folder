import datetime

current = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
# Greeting and notification of use of bio information.
print(
    "Hello, This is BMI calculator that analyses your obesity based on your weight and height.\nThis program requires your body weight and height.\nIf you agree to provide your bio information, please type 'Y'.\nIf you don't agree, then please type 'N' and then program will no longer run."
)
# If a user agrees, program runs.
# If a user disagrees, program ends.
agreement = str(
    input("# Do you agree to provide your body weight and height? information? (Y/N)\n")
)

# Possible input including both positive and negative answers.
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

# Predictable positive responses.
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
    # Program runs only under agreement response.
    print(f"[You agreed to provide your bio information at {current}]")
    # Asking which measure system prefers.
    system_preference = input(
        "If you prefer yard-pound system, please type 'Y'.\nFor metric system, please type 'M'\n"
    )
    while (
        system_preference != "Y"
        and system_preference != "y"
        and system_preference != "M"
        and system_preference != "m"
    ):
        system_preference = input("Please input valid code (Y/M)\n")
    # When the prefered system is Yard-pound system.
    if system_preference == "Y" or system_preference == "y":
        print("Yard-pound system confirmed")
        weight = input("Please input your body weight. (lb)\n")

        # Checking if weight is a float.
        # if not, while loop on input until weight is a float.
        while not weight.replace(".", "", 1).isdigit() or float(weight) < 1:
            weight = input(
                "Please input your body weight with numbers and decimal point.(lb)\n"
            )
        print(f"Weight: {weight} lb, confirmed")

        # Checking if feet is a float.
        # if not, while loop on input until feet is a float.
        print(
            "Notice: When you input your height, please input feet and inch respectively."
        )
        feet = input("Please input your height. (Feet)\n")
        while not feet.isdigit() or float(feet) < 1:
            feet = input(
                "Please input your feet value with only positive numbers and without decimal point.\n"
            )
        print(feet, "feet, confirmed.")

        # Checking if inch is a float.
        # if not, while loop on input until inch is a float
        inch = input("Please input your height. (Inch)\n")
        while inch > 11:
            inch = input("Please input your inch value minimum 1 and maximum 11.\n")
        while not inch.isdigit():
            inch = input("Please input your inch value with only numbers.\n")
        print(feet, "feet", inch, "inch. Confirmed.")
        height = feet * 12 + inch

    elif system_preference == "M" or system_preference == "m":
        print("Metric system confirmed")

elif agreement.lower() in ("n", "no", "disagree"):
    print("You didn't agree to provide your bio information. Unable to continue.")
