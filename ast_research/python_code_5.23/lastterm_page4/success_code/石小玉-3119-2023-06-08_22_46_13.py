nums=eval(input())
for x in nums:
    while nums.count(x)>1:
        nums.remove(x)
print(nums)
