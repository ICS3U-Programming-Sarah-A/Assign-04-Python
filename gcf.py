#!/usr/bin/env python3

# Created by: Sarah
# Created on: Apr, 20, 2022
# This program asks the user to enter a number. It then displays the
# square of each number from 0 until that user_number using for loops.


# A function that allows the user to play again.
def ask_again():
    user_ask = input("Would you like to find the GCF of two numbers, (y/n): ")
    # checks to see if user entered yes or no, then executes their choice.
    if user_ask == "y" or user_ask == "Y":
        main()
    elif user_ask == "n" or user_ask == "N":
        print("Thanks for playing!")
    else:
        print("Please enter either or being (y/n). ")
        # returns the funcition
        return ask_again()


def main():
    # initialize the loop counter
    counter = 0

    # get the user number as a string
    print("Today, we will be calcuating the GCF of two given numbers.")
    print("")
    user_num_1_string = input("Enter the first whole number: ")
    user_num_2_string = input("Enter the second whole number: ")
    print("")

    try:
        # converts user input to integer
        user_num_int = int(user_num_1_string)
        try:
            user_num2_int = int(user_num_2_string)

        # sets a range.
            if user_num_int and user_num2_int >= 0:
                # calculates the gcf of the two numbers user has entered and then
                # displays it
                for counter in range(user_num_int, 0, -1):
                    if user_num_int % counter == 0 and user_num2_int % counter == 0:
                        break
                print("The GCF of {} and {} is {}."
                              .format(user_num_int, user_num2_int, counter)) 
                print("")
                ask_again()
            else:
                print("Invalid enteries. Please enter a whole number.")
                print("")
                ask_again()
        except Exception:
           print("{} is not a valid number.".format(user_num_2_string))
           ask_again()
    # handles any possible errors.
    except Exception:
        print("{} is not a valid number.". format(user_num_1_string))
        ask_again()


if __name__ == "__main__":
    ask_again()
