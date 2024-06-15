nums=eval(input())
a=max(nums)
b=min(nums)
for i in nums:
    if i==a or i==b:
        nums.remove(i)
print(nums)
