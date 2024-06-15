def maxsum(a):
    a.sort()
    c = a[0:-1:2]
    d = sum(c)
    return d




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

