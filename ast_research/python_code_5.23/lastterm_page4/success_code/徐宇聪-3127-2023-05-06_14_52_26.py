n = eval(input())
nums = [x for x in range(1,n+1)]
new_nums = []
for i in range(1,len(nums)):
    new_nums.append(nums[i])
new_nums.append(nums[0])
print(new_nums)
