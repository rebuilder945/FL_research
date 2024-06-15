nums=eval(input())
n,m=eval(input())
x=nums[n-1]
y=[x]*m
nums.extend(y)
print(nums)
