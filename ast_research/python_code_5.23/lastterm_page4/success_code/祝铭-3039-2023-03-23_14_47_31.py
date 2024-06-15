nums = eval(input())
numscopy=nums[:]
ma=max(numscopy)
mi=min(numscopy)
for x in numscopy:
    if x==ma or x==mi:
        nums.remove(x)
print(nums)
