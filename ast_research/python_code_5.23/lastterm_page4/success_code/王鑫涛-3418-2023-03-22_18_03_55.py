def maxsum(a):
    b = a.sort
    c = b[0:-1:2]
    d = sum(c)
    return d




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

