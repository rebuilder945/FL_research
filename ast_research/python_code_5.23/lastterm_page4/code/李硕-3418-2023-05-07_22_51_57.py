del maxsum(t):
    t.sort()
    a=t[0::2]
    d=sum(a)
    return d




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

