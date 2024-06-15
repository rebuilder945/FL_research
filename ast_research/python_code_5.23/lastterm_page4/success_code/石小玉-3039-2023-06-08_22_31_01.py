nums=eval(input())
x=max(nums)
y=min(nums)
for i in nums:
    while i==x or i==y:
        nums.remove(i)
    else:
        pass
print(nums)
