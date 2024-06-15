def maxsum(nums):
    nums.sort(reverse=True)
    c = nums[1]+nums[3]
    return c




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

