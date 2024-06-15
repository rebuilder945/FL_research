nums=eval(input())
m,n=eval(input())
if m<=n<=len(nums)-1:
    del nums[m:n]
    print(nums)
elif n<m<=len(nums)-1:
    del nums[n:m]
    print(nums)
else: print("error")

