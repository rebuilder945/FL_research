def maxsun(a):
    a.sort()
    b=a[::2]
    c=sum(b)
    return c




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

