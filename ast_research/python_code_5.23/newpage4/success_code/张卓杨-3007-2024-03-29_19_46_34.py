nums = list(eval(input()))
num = eval(input())
nlen = len(nums)
if n>=nlen or n<-1*nlen:
    print("error")
else:
    append  =[nums[n]]*m
    nums = nums+append
    print(nums)

