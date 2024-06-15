nums= input().split(',')
n, m = map(int, input().split(','))
if abs(n) < len(nums):
    ls=[nums[n]*n]
    nums=nums+ls
    print(nums)
else:
    print("error")






