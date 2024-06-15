def maxsum(m):
    m=m.sort()
    s=sum(m[::2])
    return s




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

