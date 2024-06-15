def a_max_number(nums):
    nums = list(map(str,nums))
    nums.sort(key=lambda x:x*3,reverse=True)
    return int(''.join(nums))
nums = []
result = a_max_number(nums)
print(result)
