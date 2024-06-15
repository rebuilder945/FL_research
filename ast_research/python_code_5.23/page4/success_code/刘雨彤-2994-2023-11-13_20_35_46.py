nums=list(eval(input()))
n,m=eval(input())
if n not in range(len(nums)):
    print("error")
else:
    add=[nums[n]]*m
    res=nums+add
    print(res)
