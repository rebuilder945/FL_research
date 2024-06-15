nums=eval(input())
n,m=eval(input())
if n not in range(len(nums)) or m not in range(len(nums)):
    print("error")
else:
    del nums[n:m]
    print(nums)

