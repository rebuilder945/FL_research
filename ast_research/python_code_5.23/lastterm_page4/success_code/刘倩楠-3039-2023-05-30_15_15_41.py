nums=eval(input())
a=max(nums)
b=min(nums)
for x in range(len(nums)):
    c=nums[x]
    if c==a or c==b:
        nums.remove(c)
print(nums)
