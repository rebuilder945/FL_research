nums=eval(input())
max_num = max(nums) 
min_num = min(nums) 
nums = [num for num in nums if num != max_num and num != min_num]  
print(nums)
