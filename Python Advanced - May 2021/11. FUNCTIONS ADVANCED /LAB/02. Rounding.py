def round_iter_el(nums):
    result = [round(el) for el in nums]
    return result


nums_list = map(float, input().split())
print(round_iter_el(nums_list))
