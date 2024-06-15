def maxsum(nums):
    nums.sort()
    v=0
    for s in range(len(nums)):
        if s%2==0:
            v+=nums[s]
    return v




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

