def max_number(nums):
    nums = sorted(nums, key=lambda x: str(x), reverse=True)
    result = ''.join(str(num) for num in nums)
    return int(result)

nums = [0, 1, 2, 3, 2]
print(max_number(nums))

