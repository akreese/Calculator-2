"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
while True:
    calculations = input("Please enter your equation> ")
    tokens = calculations.split(' ')
    if tokens[0] == 'q':
        print("You are now exiting")
        break
    equation = tokens[0]
    num1 = tokens[1]


