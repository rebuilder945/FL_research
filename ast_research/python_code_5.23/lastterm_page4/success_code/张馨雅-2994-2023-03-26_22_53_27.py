nums=eval(input())
nums1=list(nums)
n,m=eval(input())
b=[nums[n]]
print(b)
if n<=len(nums):
    a=b*3
    c=nums1+a
    print(c)
else:
    print('error')
