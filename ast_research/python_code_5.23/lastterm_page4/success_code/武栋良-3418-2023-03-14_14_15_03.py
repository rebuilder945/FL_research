def maxsum(nums):
    nums.sort()
    for x in nums:
        s = 0
        if not x%2:
            s = s+x
    return s




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

