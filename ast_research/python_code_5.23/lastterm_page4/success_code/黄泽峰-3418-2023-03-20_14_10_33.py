def maxsum(nums):
    nums.sort()
    numss=nums[:2]
    s = sum(numss)
    return s




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

