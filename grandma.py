# Created by Ryan Nguyen
# Created on December 2020
# This program asks the user their age and checks if
#   it is between 25 and 40


def main():
    # This function checks age

    # input
    age_as_string = input("Enter age: ")
    print("")

    # process + output
    try:
        age_as_number = int(age_as_string)
        if age_as_number < 25:
            print("Too young")
        elif age_as_number >= 25 and age_as_number <= 40:
            print("You're the perfect age")
        elif age_as_number > 40:
            print("Too old")
        else:
            print("No clue")
    except Exception:
        print("Not an age")


if __name__ == "__main__":
    main()
