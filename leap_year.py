#!/usr/bin/env python3

# Created by: Caylee Annett
# Created on: May 2021
# This program tells the user if it is a leap year and uses nested
#    if statements


def main():
    # This function tells the user if it is a leap year

    # Input
    print("This program will tell you if it is a leap year.")
    year_as_string = input("Enter the year: ")
    print("")

    # Process & Output
    try:
        year_as_integer = int(year_as_string)

        if year_as_integer % 4 == 0:
            if year_as_integer % 100 == 0 and year_as_integer % 400 != 0:
                print("{} is a not leap year.".format(year_as_integer))
            else:
                print("{} is a leap year!".format(year_as_integer))
        else:
            print("{} is not a leap year.".format(year_as_integer))
    except Exception:
        print("{} is not a valid input.".format(year_as_string))
    print("\nDone.")


if __name__ == "__main__":
    main()
