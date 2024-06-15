nums=eval(input())
nums1=list(nums)
n,m=eval(input())
if n<=len(nums):
    b=[nums[n]]
    a=b*m
    c=nums1+a
    print(c)
else:
    print('error')
