def largest_number(nums):
    nums = sorted(nums, key=lambda x: str(x), reverse=True)
    result = ''.join(str(num) for num in nums)
    return int(result) if result[0] != '0' else 0

nums = [0, 1, 2, 3, 2]
print(largest_number(nums))

