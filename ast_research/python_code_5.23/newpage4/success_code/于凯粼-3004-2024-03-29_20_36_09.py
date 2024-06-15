nums=eval(input())
a=max(nums)
b=min(nums)
while a in nums:
    nums.remove(a)
while b in nums:
    nums.remove(b)
print(nums)
