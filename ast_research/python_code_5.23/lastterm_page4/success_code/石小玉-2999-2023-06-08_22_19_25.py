nums=input().split()
n,m=input().split()
a=int(n)
b=int(m)
x=nums[n]
nums[n]=nums[m]
nums[m]=x
print(nums)

