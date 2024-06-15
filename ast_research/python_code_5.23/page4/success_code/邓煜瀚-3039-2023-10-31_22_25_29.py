nums=eval(input())
a=max(nums)
b=min(nums)
c=nums.copy()
for num in nums:
    if num == a or num == b:
        c.remove(num)
print(c)
