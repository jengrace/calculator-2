"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here


""" 
while true:
    input = take user input
    tokens = input.split(" ")
    oper = token[0]


    if q or quit:
        quit
    elif oper in [all operations]:
        num1 = int(tokens[1]
        try:
            num2 = tokens[2]
            try:
                num1 = int(num1)
                num2 = int(num2)
            except ValueError:
                print "not valid input"
                continue
        except IndexError:
            try:
                num1 = int(num1)
            except ValueError:
                print "not valid input"
            num2 = None

        try: 

        if oper == +:
            arithmetic.add()
        if ...... rest of operators 

    else:
        print "sorry i dnt understand"
        continue

"""

"""
make one print statement
let user use upper and lower case
wrap everything in a function 
make function for validation 
"""

while True:
    user_input = raw_input("Enter calculation: \n  >   ")
    tokens = user_input.split(" ")
    oper = tokens[0]

    if oper in ["q", "quit"]:
        break
    elif oper in ["+", "-", "*", "/", "square", "cube", "pow", "mod"]:
        num1 = tokens[1]
        try:
            num2 = tokens[2]
            try:
                num1 = int(num1)
                num2 = int(num2)
            except ValueError:
                print "Please provide integers to calculate"
                continue
        except IndexError:
            try:
                num1 = int(num1)
            except ValueError:
                print "Please provide integers to calculate"
                continue
            num2 = None
        result = ""
        if oper == "+":
            result = add(num1, num2)
        elif oper == "-":
            result = subtract(num1, num2)
        elif oper == "*":
            result = multiply(num1, num2)
        elif oper == "/":
            result = divide(num1, num2)
        elif oper == "square":
            result = square(num1)
        elif oper == "cube":
            result = cube(num1)
        elif oper == "pow":
            result = power(num1, num2)
        elif oper == "mod":
            result = mod(num1, num2)
        print "  =  %i" % (result)

    else:
        print "Sorry I didnt understand what you wrote"











