def maxsum(a):
    b=a.sort()
    c=len(b)
    d=b[0:2:c]
    f=sum(d)
    return f




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

