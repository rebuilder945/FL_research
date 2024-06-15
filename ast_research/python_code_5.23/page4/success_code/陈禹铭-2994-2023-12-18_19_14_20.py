nums= input().split(',')
n, m = map(int, input().split(','))
if abs(n) < len(nums):
    ls=[nums[n]]*m
    nums=nums+ls
    nums=[int(i) for i in nums]
    print(nums)
else:
    print("error")






