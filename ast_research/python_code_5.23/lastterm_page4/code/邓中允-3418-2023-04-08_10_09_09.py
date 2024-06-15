def maxsum(y):
    n=len(y)//2
    pairs=[y[i],y[i+n] for i in range(n)]
    maxsum=[min(pair) for pair in pairs]
    return maxsum




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

