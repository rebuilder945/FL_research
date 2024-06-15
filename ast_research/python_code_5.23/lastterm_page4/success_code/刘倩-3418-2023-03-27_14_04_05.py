def maxsum(nums):
    a = sorted(nums)
    return sum(a[::2])




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

