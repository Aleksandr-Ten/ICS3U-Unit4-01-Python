#!/usr/bin/env python3

# Created by: Aleksandr Ten
# Created on: April 2022
# This program calculates the total of sequential numbers starting from 0


def main():
    # this function uses a loop

    # this is to keep track of the loop and calculate the total
    loop_counter = 0
    total = 0

    # input
    positive_int_string = input("Enter a positive integer: ")

    # process & output
    try:
        positive_int = int(positive_int_string)
        while loop_counter < positive_int:
            loop_counter = loop_counter + 1
            total = total + loop_counter
        else:
            print(
                "The total of all positive numbers from 1 to {0} is {1}.".format(
                    positive_int, total
                )
            )
    except Exception:
        print("Invalid input")
    finally:
        print("\nDone")


if __name__ == "__main__":
    main()
