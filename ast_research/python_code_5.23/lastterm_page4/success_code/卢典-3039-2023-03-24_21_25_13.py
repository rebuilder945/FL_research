nums = input().split()  
nums = [int(num) for num in nums]  
max_num = max(nums) 
min_num = min(nums) 
nums = [num for num in nums if num != max_num and num != min_num]  
print((map(str, nums)))
