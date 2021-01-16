"""Functions for common math operations."""


def add(numbers):
    """Return the sum of the two input integers."""
    counter = 0
    
    for num in numbers:
        counter += num

    return counter


def subtract(numbers):
    """Return the second number subtracted from the first."""
    counter = 0
    x = 1
    for num in numbers:
        counter = numbers[x]
        counter -= num
        x = x + 1

    return counter


def multiply(num1, num2):

    counter = 1
    
    for num in numbers:
        counter *= num

    return counter


def divide(num1, num2):
    """Divide the first input by the second and return the result."""

    return float(num1) / num2


def square(num1):
    """Return the square of the input."""

    return num1 * num1


def cube(num1):
    """Return the cube of the input."""

    return num1 * num1 * num1


def power(num1, num2):
    """Raise num1 to the power of num2 and return the value."""

    return num1 ** num2  # ** = exponent operator


def mod(num1, num2):
    """Return the remainder of num1 / num2."""

    return num1 % num2
