nums=list(eval(input()))
n,m=eval(input())
nlen = lenn(nums)
if n >=nlen or n<-1*nlen:
    print("error")
else:
    append_l=[nums[n]]*m
    nums=nums+append_l
    print(nums)
