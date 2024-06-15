def find_unique(nums):
    unique_dict = {}
    for num in nums:
        if num in unique_dict:
            unique_dict[num] += 1
        else:
            unique_dict[num] = 1
    unique_nums = []
    for num, count in unique_dict.items():
        if count == 1:
            unique_nums.append(num)
    if len(unique_nums) == 0:
        return False
    else:
        return sorted(unique_nums)

