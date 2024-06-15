def maxsum(y):
    y.sort()
    kong = []
    for i in range(0,len(y),2):
        p = i+1
        c = min(y[i],y[p])
        kong.append(c)
    return sum(kong)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

