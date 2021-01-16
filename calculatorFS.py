"""CLI application for a prefix-notation calculator."""

from arithmeticFS import (add, subtract, multiply, divide, square, cube,
                        power, mod)

def calculator():
    while True:
        try:
            read_input = input("Enter your equation: ")
            tokens = read_input.split(" ")
            # have to float every int skipping index[0] and it 
            # creates a list with the operation and integers
            tokens2 = (float(i) for i in tokens[1:]) 
            if "q" in tokens:
                print("Quit")
                break

            else:
                if len(tokens) <= 2:
                    print("Please enter the correct amount of inputs.")
                        
                elif tokens[0] == "+":  
                    answer = add(tokens2)
                    print(float(answer))
                elif tokens[0] == "-":
                    answer = subtract(tokens2)
                    print(answer)
                elif tokens[0] == "*":
                    answer = multiply(float(tokens[1]), float(tokens[2]))
                    print(answer)
                elif tokens[0] == "/":
                    answer = divide(float(tokens[1]), float(tokens[2]))
                    print(answer)
                elif tokens[0] == "square":
                    answer = square(float(tokens[1]))
                    print(answer)
                elif tokens[0] == "cube":
                    answer = cube(float(tokens[1]))
                    print(answer)
                elif tokens[0] == "pow":
                    answer = power(float(tokens[1]), float(tokens[2]))
                    print(answer)
                elif tokens[0] == "mod":
                    answer = mod(float(tokens[1]), float(tokens[2]))
                    print(answer)
                else:
                    print("Please type in an operator and 2 numbers separated by spaces.")
        except ValueError:
            print('That is not a number.')
calculator() 

'''
if len(tokens) <= 2:
    if tokens[0] == 'mod' or token == 'pow' or cube....
        answer = mod(float(tokens[1]), float(tokens[2]))
        answer = power(float(tokens[1]), float(tokens[2]))
        
'''