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
while not agreement.lower() in ("y", "yes", "agree", "n", "no", "disagree"):
    agreement = input("Please input valid code (Y/N)\n")

# Predictable positive responses.
if agreement.lower() in ("y", "yes", "agree"):
    # Program runs only under agreement response.
    print(f"[You agreed to provide your bio information at {current}]")
    # Asking which measure system prefers.
    system_preference = input(
        "If you prefer yard-pound system, please type 'Y'.\nFor metric system, please type 'M'.\n"
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
        # if not, while loop on input until inch is a float.
        inch = input("Please input your height. (Inch)\n")
        while (
            not inch.replace(".", "", 1).isdigit()
            or float(inch) >= 12
            or float(inch) < 1
        ):
            inch = input("Please input your inch value with only numbers.\n")
        print(feet, "feet", inch, "inch. Confirmed.")

        # Converting feet to inch.
        height = float(feet) * 12 + float(inch)
        # BMI index calculation and printing the value.
        BMI = (float(weight) / float((height ** 2))) * 703
        print("Your BMI index is", round(BMI, 1))

        # Providing additional information based on BMI index.
        if BMI < 18.5:
            print("Your are underweight")
        elif BMI >= 18.5 or BMI < 25.0:
            print("Your weight is normal")
        elif BMI >= 25.0 or BMI < 30.0:
            print("You are overweight")
        elif BMI >= 30.0:
            print("You are obese")

    # When the metric system is prefered.
    elif system_preference == "M" or system_preference == "m":
        print("Metric system confirmed")
        weight = input("Please input your body weight. (Kg)\n")

        # Checking if weight is a float.
        # if not, while loop on input until weight is a float.
        while not weight.replace(".", "", 1).isdigit() or float(weight) < 1:
            weight = input(
                "Please input your body weight with numbers and decimal point.(Kg)\n"
            )
        print(f"Weight: {weight} Kg, confirmed")

        # Checking if height is a float.
        # if not, while loop on input until feet is a float.
        print("Notice: Please input your height with centi-meter (cm).")
        height = input("Please input your height. (cm)\n")
        while not height.replace(".", "", 1).isdigit() or float(height) < 1:
            height = input("Please input your cm value with only positive numbers.\n")
        print(height, "cm, confirmed.")
        height = float(height) / 100
        BMI = float(weight) / (height ** 2)
        print("Your BMI index is", round(BMI, 1))

        # Providing additional information based on BMI index.
        if BMI < 18.5:
            print("Your are underweight")
        elif BMI >= 18.5 or BMI < 25.0:
            print("Your weight is normal")
        elif BMI >= 25.0 or BMI < 30.0:
            print("You are overweight")
        elif BMI >= 30.0:
            print("You are obese")

elif agreement.lower() in ("n", "no", "disagree"):
    print("You didn't agree to provide your bio information. Unable to continue.")
