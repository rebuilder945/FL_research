nums=list(eval(input()))
n,m=eval(input())
s=len(nums)
if n>0 and s>=n:
    nums2=nums[n]*m
    nums3=nums+nums2
    print(nums3)
else:
    print("error")
    



