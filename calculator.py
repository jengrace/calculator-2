"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here




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

    oper = tokens[0].lower()
    result = ""

    if oper in ["q", "quit"]:
        break

    elif oper in ["+", "-", "*", "/", "square", "cube", "pow", "mod"]:
        nums = tokens[1:]
        int_nums = validated_tokens(nums)

        if int_nums is None:
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

        elif oper == "pow":
            result = power(int_nums)
        elif oper == "mod":
            result = mod(int_nums)

        elif oper in ["square", "cube"]:
            if len(int_nums) > 1:
                print "These operations only takes one integer"
                continue

            if oper == "square":
                result = square(int_nums)
                print result
            elif oper == "cube":
                result = cube(int_nums)

        print "  =  %s" % (result)

    else:
        print "Sorry I didnt understand what you wrote"










