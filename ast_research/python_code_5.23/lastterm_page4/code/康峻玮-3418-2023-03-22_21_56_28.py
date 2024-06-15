def maxsum(y)
    z = list(y)
    z.sort()
    b = z[::2]
    c = sum(b)
    return c





nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

