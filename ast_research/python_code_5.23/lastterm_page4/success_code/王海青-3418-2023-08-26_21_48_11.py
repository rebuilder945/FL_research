def maxsum(nums):
    nums.sort()
    for i in nums[:]:
        v=nums[0]+nums[-2]
    return v




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

