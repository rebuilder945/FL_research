def create_largest_number(nums):
    nums.sort(reverse=True)  
    largest_number = int(''.join(map(str, nums)))  
    return largest_number


nums = input()
nums = [int(num) for num in nums.split(",")]
result = create_largest_number(nums)
print(result)

