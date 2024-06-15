def maxsum(a):
    a.sort()
    b = sum(a[::2])
    return b




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

