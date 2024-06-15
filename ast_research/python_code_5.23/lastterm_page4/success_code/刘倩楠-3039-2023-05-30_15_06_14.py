nums=input()
a=int(max(nums))
b=int(min(nums))
for i in list(range(len(nums))):
    if int(nums[i])==a or int(nums[i])==b:
        nums.remove(nums[i])
print(nums)
