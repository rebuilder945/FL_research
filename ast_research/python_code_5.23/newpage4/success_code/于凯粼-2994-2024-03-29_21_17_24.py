nums=list(eval(input()))
n,m=eval(input())
nlen=len(nums)
if n>=nlen or n<-1*nlen:
    print("error")
else:
    appendl=[nums[n]]*m
    nums=nums+appendl
    print(nums)

