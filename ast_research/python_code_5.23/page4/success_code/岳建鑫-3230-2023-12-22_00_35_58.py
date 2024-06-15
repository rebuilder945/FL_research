def create_largest_number(nums):
    nums.sort(reverse=True)  
    largest_number = int(''.join(map(str, nums)))  
    return largest_number


nums =input()
result = create_largest_number(nums)
print(result)

