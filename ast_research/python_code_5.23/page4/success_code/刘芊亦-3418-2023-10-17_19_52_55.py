def maxsum(nums):
    nums.sort()
    pairs=list(zip(nums[:-1],nums[1:]))
    maxsum=sum(min(pair) for pair in pairs)
    return maxsum




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

