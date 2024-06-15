nums = eval(input())
ma=max(nums)
mi=min(nums)
for x in nums:
    if x==ma or x==mi:
        nums.remove(x)
print(nums)
