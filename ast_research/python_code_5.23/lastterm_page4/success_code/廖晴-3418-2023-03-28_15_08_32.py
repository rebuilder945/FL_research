def maxsum(z):
    z.sort()
    L=len(z)
    N=L//2
    a=z[0]
    b=z[N]
    sum=a+b
    return sum




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

