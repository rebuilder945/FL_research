def maxsum(nums):
    nums.sort()
    a=sum(nums[::2])
    return a




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

