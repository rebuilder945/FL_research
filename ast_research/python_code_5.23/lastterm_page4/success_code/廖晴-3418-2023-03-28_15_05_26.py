def maxsum(z):
    z.sort()
    a=min(z)
    L=len(z)
    S=L//2
    del z[0:S]
    b=min(z)
    sum=a+b
    return sum




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

