nums=eval(input())
n,m=eval(input())
s=len(nums)
if s>=n:
    nums2=nums[n-1]*m
    nums3=nums+nums2
    print(nums3)
else:
    print("error")
    



