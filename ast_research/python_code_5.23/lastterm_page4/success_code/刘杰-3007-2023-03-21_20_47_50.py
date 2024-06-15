nums=eval(input())
m,n=eval(input())
if n<=m<=len(nums)-1:
    del nums[n:m]
    print(nums)
else:
    print("error")
