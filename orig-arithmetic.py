def add(num1, num2):
    """Return the sum of two numbers"""
    my_sum = num1 + num2
    return my_sum


def subtract(num1, num2):
    """Return the difference of two numbers"""
    my_diff = num1 - num2
    return my_diff


def multiply(num1, num2):
    """Return the product of two numbers"""
    my_prod = num1 * num2
    return my_prod


def divide(num1, num2):
    """Return the quotient of two numbers as a float"""
    my_div = float(num1)/num2
    return my_div


def square(num):
    """Return the square of a number"""
    my_sqr = num*num
    return my_sqr


def cube(num):
    """Return the cube of a number"""
    my_cube = num*num*num
    return my_cube


def power(num, exponent):
    """Return num raised to the power of exponent"""
    my_exp = num ** exponent
    return my_exp


def mod(num1, num2):
    """Return remainder of num1 divided by num2"""
    my_mod = num1 % num2
    return my_mod
