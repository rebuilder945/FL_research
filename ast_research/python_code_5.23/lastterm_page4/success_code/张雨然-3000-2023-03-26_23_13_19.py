nums=str(input()).split()
n,m=map(int,input().split())
temp=nums[n]
nums[n]=nums[m]
nums[m]=temp
print(nums)
