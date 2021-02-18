nums_as_string = input().split(", ")


nums = [int(el) for el in nums_as_string]
# with map - the fastest
# nums_map = list(map(lambda el: int(el), nums_as_string))
# nums_map = list(map(int, nums_as_string))

filtered_nums = [index for index in range(len(nums)) if nums[index] % 2 == 0]
# filtered_num_filter = [nums.index(el) for el in list(filter(lambda el: el % 2 ==0, nums))]
filtered_nums_map = list(map(lambda el: nums.index(el), list(filter(lambda el: el % 2 ==0, nums))))
print(filtered_nums_map)
