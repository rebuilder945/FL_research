def maxsum(a):
    a.sort()
    c=len(a)
    d=a[0:c-1:2]
    f=sum(d)
    return f




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

