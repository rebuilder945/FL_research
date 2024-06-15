nums=eval(input())
max_value=max(nums)
min_value=min(nums)
filtered_nums=[num for num in nums if num !=max_value and num !=min_value]
print(filtered_nums)
