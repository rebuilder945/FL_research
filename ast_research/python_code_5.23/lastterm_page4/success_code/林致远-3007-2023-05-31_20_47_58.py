nums =  eval(input())
n,m = eval(input())
if m > len(nums) or n >len(nums):
    print('error')
else:
    del nums[n:m]
    print(nums)
