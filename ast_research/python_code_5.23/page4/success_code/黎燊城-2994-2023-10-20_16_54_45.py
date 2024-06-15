nums=list(eval(input()))
a,b=eval(input())
c=len(nums)
if a>=c  or c < -1*c:
    print("error")
else:
    d =[nums[a]]*b
    nums = nums+d
    print(nums)
