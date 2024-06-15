nums=eval(input())
a=max(nums)
b=min(nums)
for i in range(nums):
    if i==a or (i==b and i!=a):
        nums.remove(i)
print(nums)
    
