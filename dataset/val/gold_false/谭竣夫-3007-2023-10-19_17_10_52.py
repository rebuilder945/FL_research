nums=eval(input())
n,m=eval(input())
lst=n,m
if m<=len(lst):
    del nums[n:m]
    print(nums)
else:
    print("error")
