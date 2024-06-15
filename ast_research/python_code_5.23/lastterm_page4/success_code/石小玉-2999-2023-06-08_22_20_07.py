nums=input().split()
n,m=input().split()
a=int(n)
b=int(m)
x=nums[a]
nums[a]=nums[b]
nums[b]=x
print(nums)

