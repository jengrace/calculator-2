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


def validated_tokens(nums):
    """ validates that inputs can be ints and creates a list of them as ints
    """

    int_list = []
    for num in nums:
        try:
            int_num = int(num)
            int_list.append(int_num)
        except ValueError:
            return None
    return int_list


while True:
    user_input = raw_input("Enter calculation: \n  >   ")
    tokens = user_input.split(" ")

    oper = tokens[0]
    result = ""


    if oper in ["q", "quit"]:
        break


    elif oper in ["+", "-", "*", "/", "square", "cube", "pow", "mod"]:
        nums = tokens[1:]
        int_nums = validated_tokens(nums)

        if int_nums == None:
            print "Please only enter integers for us to calculate"
            continue


        if oper == "+":
            result = add(int_nums)
        elif oper == "-":
            result = subtract(int_nums)
        elif oper == "*":
            result = multiply(int_nums)
        elif oper == "/":
            result = divide(int_nums)
        
        # elif oper == "pow":
        #     result = power(num1, num2)
        # elif oper == "mod":
        #     result = mod(num1, num2)
        if oper in ["square", "cube"]:
            if len(int_nums) > 1:
                print "These operations only take one integer"
                continue

        elif oper == "square":
            result = square(int_nums)
            print result
        elif oper == "cube":
            result = cube(int_nums)

        print "  =  %s" % (result)

    else:
        print "Sorry I didnt understand what you wrote"










