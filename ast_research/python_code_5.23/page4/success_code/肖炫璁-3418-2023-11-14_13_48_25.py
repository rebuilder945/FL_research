def maxsum(nums):
    nums.sort()
    result = sum(nums[::2])
    return result





nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

