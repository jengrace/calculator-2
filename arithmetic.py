def add(nums):
    result = 0
    for num in nums:
        result = result + num
    return result


def subtract(nums):
    result = 0
    for num in nums:
        result = result - num
    return result


def multiply(nums):
    if len(nums) == 0:
        return 0
    result = 1
    for num in nums:
        result = result * num
    return result


def divide(nums):
    # Need to turn at least argument to float for division to
    # not be integer division
    if len(nums) == 0:
        return 0
    result = float(nums[0])
    for num in nums[1:]:
        result = result/num
    return result


def square(nums):
    # Needs only one argument
    num = nums[0]
    result = num * num
    return result


def cube(nums):
    # Needs only one argument
    num = nums[0]
    result = num * num * num
    return result


def power(nums):
    # ** = exponent operator
    if len(nums) == 0:
        return 0
    result = nums[0]
    for num in nums[1:]:
        result = result ** num
    return result


def mod(nums):
    # Takes the mod of the numbers in order
    if len(nums) == 0:
        return 0
    result = nums[0]
    for num in nums[1:]:
        result = result % num
    return result
