def maxsum(x):
    z=0
    for i in range(len(x)):
        for j in range(len(x)):
            if (x[i]+x[j]) > z and i!=j:
                z=x[i]+x[j]
    return z




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

