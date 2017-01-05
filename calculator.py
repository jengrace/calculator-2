"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from orig_arithmetic import *


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


def my_reduce(func, lst):
    """ take a function and a list, and iterativly call the function on the list
    returns end result
    """
    if len(lst) == 0:
        return 0

    result = lst[0]
    for item in lst[1:]:
        result = func(result, item)

    return result



while True:
    user_input = raw_input("Enter calculation: \n  >   ")
    user_input = user_input.rstrip().lstrip()
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
            result = my_reduce(add, int_nums)
        elif oper == "-":
            result = my_reduce(subtract, int_nums)
        elif oper == "*":
            result = my_reduce(multiply, int_nums)
        elif oper == "/":
            result = my_reduce(divide, int_nums)

        elif oper == "pow":
            result = my_reduce(power, int_nums)
        elif oper == "mod":
            result = my_reduce(mod, int_nums)

        elif oper in ["square", "cube"]:
            if len(int_nums) > 1:
                print "These operations only takes one integer"
                continue

            single_num = int_nums[0]

            if oper == "square":
                result = square(single_num)
                print result
            elif oper == "cube":
                result = cube(single_num)

        print "  =  %s" % (result)

    else:
        print "Sorry I didnt understand what you wrote"










