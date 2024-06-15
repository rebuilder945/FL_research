def maxsum(a):
    a.sort(reverse = True)
    b = a[1::2]
    c = sum(b)
    return c





nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

