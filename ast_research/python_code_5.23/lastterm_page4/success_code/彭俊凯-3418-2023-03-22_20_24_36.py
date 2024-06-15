def maxsum(x):
    x.sort()
    a=x[0:len(x):2]
    b=sum(a)
    return b




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

