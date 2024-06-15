def maxsum(nums):
    nums.sort()
    s = 0
    for x in nums:
        if nums.enumerate(x) % 2 == 0:
            s = s+x
    return s




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

