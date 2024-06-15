nums=list(eval(input()))
n,m=eval(input())
if n>=len(nums) or n<-1*len(nums):
    print("error")
else:
    add=[nums[n]]*m
    res=nums+add
    print(res)
