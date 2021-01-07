"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
# define the function
# while loop:
# tokenize input

    # if first token is "q" break

    # else

def calculator():
    while True:
        read_input = input("Enter your equation: ")
        tokens = read_input.split(" ")
        # tokens[1] = num1
        # tokens[2] = num2

        if "q" in tokens:
            print("Quit")
            break

        else:
            if tokens[0] == "+":  
                answer = add(float(tokens[1]), float(tokens[2]))
                print(answer)
            if tokens[0] == "-":
                answer = subtract(float(tokens[1]), float(tokens[2]))
                print(answer)
            if tokens[0] == "*":
                answer = multiply(float(tokens[1]), float(tokens[2]))
                print(answer)
            if tokens[0] == "/":
                answer = divide(float(tokens[1]), float(tokens[2]))
                print(answer)
            if tokens[0] == "square":
                answer = square(float(tokens[1]))
                print(answer)
            if tokens[0] == "cube":
                answer = cube(float(tokens[1]))
                print(answer)
            if tokens[0] == "pow":
                answer = power(float(tokens[1]), float(tokens[2]))
                print(answer)
            if tokens[0] == "mod":
                answer = mod(float(tokens[1]), float(tokens[2]))
                print(answer)
calculator()