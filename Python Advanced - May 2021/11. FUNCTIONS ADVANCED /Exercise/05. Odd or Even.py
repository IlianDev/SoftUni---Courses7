def sum_nums(nums):
    odds = []
    evens = []

    for num in nums:
        if num % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)


# command = input()
numbers = list(map(int, input().split()))
print(sum_nums(numbers))
