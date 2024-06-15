def maxsum(x):
    x.sort()
    e=0

    for i in range (0,int(len(x)/2)):
        d=[]
        d.append(x[2*i])
        d.append(x[2*i+1])
        c=min(d)
        e=e+c

    return e





nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

