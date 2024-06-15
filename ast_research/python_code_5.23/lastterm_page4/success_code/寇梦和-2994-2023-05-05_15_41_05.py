nums=list(eval(input()))
n,m=eval(input())
s=len(nums)
if n>0 and n>=s:
    print("error")
elif n<0 and abs(n)>s:
    print("error")
else:
    nums2=[nums[n]]*m
    nums3=nums+nums2
    print(nums3)
    



