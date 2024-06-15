def maxsum(z):
    z.sort()
    a=min(z)
    l=len(z)
    l=l//2
    del z[0:l]
    b=min(z)
    sum=a+b
    return sum




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

