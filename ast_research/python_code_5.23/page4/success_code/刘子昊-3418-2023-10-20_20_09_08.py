def maxsum(nums):
    nums.sort()
    v=nums[-2]+nums[-4]
    return v




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

