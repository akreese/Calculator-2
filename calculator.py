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
    else:
        equation = tokens[0]
        num1 = tokens[1]
        result = None
        if equation == '+':
            result = add(float(num1), float(tokens[2]))
        elif equation == '-':
            result = subtract(float(num1), float(tokens[2]))
        elif equation == '*':
            result = multiply(float(num1), float(tokens[2]))
        elif equation == '/':
            result = divide(float(num1), float(tokens[2]))
        elif equation == 'square':
            result = square(float(num1))
        elif equation == 'cube':
            result = cube(float(num1))
        elif equation == 'pow':
            result = power(float(num1), float(tokens[2]))
        elif equation == 'mod':
            result = mod(float(num1), float(tokens[2]))
        print(result)
        




 

