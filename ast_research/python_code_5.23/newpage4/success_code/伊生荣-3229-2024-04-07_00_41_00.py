def find_unique_elements(nums):
    unique_nums = [num for num in nums if nums.count(num) == 1]
    if unique_nums:
        return sorted(unique_nums)
    else:
        return False
