def find_unique_elements(nums):
    unique_nums = [num for num in nums if nums.count(num) == 1]
    if unique_nums:
        return sorted(unique_nums)
    else:
        return False
nums = [1, 2, 3, 4, 5, 2, 3, 4]
result = find_unique_elements(nums)
print(result)
