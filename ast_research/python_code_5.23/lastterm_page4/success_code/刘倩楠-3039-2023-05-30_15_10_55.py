nums=eval(input())
a=max(nums)
b=min(nums)
for x in nums:
    if x==a or x==b:
        nums.remove(x)
print(nums)
