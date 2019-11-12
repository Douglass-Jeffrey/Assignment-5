#!/usr/bin/env python3

# Created by: Douglass Jeffrey
# Created on: Oct 2019
# This program calculates one number to the power of another


def main():
    loopcounter = 0
    loopsum = 1

    # input Process and Output
    try:
        # input
        value_1 = int(input("Enter your first number: "))
        print("To what value would you")
        power_number = int(input("like this number be raised? "))
        # process/output
        while loopcounter < power_number:
            loopsum = loopsum * value_1
            loopcounter = loopcounter + 1
        print(str(value_1) + " to the power of " + str(power_number) + " = "
              + str(loopsum))
    except Exception:
        print("Please input only valid integers")


if __name__ == "__main__":
    main()
