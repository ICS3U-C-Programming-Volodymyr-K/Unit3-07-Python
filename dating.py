#!/usr/bin/env python3
# Created By: Volodymyr Kryzhanovskyi
# Date: 03 27, 2025
# This program creates the date answers.


def main():
    # Getting the input from user
    age_of_user = input("How old are you?")
    try:
        age_of_user = int(age_of_user)
        if age_of_user <= 0:
            print("Not a real year.")
        if age_of_user >= 25 and age_of_user <= 40:
            print("You can date my daughter")
        if  age_of_user <= 25 and age_of_user >= 0:
            print("You can't date my daughter because you are too young.")
        if age_of_user >= 40:
            print("You can't date my daughter because you are too old")
    except Exception:
        print("I don't understand.")
    finally:
        print("Nice to see you.")


if __name__ == "__main__":
    main()
