def maxsum(nums):
    nums.reverse()
    v=nums[1]+nums[3]
    return v




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

