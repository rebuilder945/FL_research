nums=eval(inout())
n,m=eval(input())
if m<=n<=len(nums)-1:
    del nums[m:n]
    print(nums)
elif n<m=len(nums)-1:
     del nums[n+1:m+1]
     print(nums)
else；
     print("error")
