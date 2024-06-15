def max_number(nums):
    nums = sorted(nums, reverse=True)  
    result = int(''.join(map(str, nums)))  
    return result

nums = input()
nums = [int(num) for num in nums.replace("[", "").replace("]", "").split(",")]
output = max_number(nums)
print(output)

