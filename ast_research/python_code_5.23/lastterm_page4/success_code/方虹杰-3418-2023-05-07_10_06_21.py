def maxsum(nums):
    nums.sort()
    sumv=sum(nums[::2])
    return sumv




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

