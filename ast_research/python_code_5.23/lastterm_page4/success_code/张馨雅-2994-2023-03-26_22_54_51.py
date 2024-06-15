nums=eval(input())
nums1=list(nums)
n,m=eval(input())
b=[nums[n]]
if n<=len(nums):
    a=b*m
    c=nums1+a
    print(c)
else:
    print('error')
