nums=eval(input())
m,n=eval(input())
if m <= n <= len(nums)-1:
    del nums[m:n]
    print(nums)
else:
    print("error")


