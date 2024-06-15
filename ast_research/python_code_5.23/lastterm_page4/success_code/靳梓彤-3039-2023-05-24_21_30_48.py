nums=eval(input())
a=max(nums)
b=min(nums)
while nums.count(a)>0:
    nums.remove(a)
while nums.count(b)>0:
    nums.remove(b)
print(nums)
