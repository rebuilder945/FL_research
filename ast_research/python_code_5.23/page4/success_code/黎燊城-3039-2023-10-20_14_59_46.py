nums=eval(input())
a=max(nums)
b=min(nums)
c=nums.copy()
for i in nums:
    if i==a or i==b:
        c.remove(i)
print(c)
