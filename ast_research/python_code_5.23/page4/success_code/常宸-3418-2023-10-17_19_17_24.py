def maxsum(nums:list):
    nums.sort()
    minv = nums[::]
    sumv = sum(minv)
    return sumv




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

