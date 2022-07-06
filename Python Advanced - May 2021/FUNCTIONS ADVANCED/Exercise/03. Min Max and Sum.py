def min_num(nums):
    return min(nums)


def max_num(nums):
    return max(nums)


def sum_nums(nums):
    return sum(nums)


numbers = [int(i) for i in input().split()]
print(f"The minimum number is {min_num(numbers)}")
print(f"The maximum number is {max_num(numbers)}")
print(f"The sum number is: {sum_nums(numbers)}")

