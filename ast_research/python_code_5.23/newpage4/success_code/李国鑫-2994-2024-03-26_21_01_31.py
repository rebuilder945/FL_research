nums = list(eval(input()))
n,m = list(eval(input()))
nlen = len(nums)
if n >= nlen or n < -1*nlen:
    print("error")
else:
    append_l = [nums[n]]*m
    nums = nums+append_l
    print(nums)

