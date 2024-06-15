def maxsum(nums):
    nums.sort()
    s=nums[::2]
    return s




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

