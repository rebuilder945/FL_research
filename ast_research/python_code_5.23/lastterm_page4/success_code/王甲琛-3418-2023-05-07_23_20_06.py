def maxsum(a):
    d=[]
    for x in a:
        d.append(x)
    d.sort()
    b=[]
    for i in range(int(len(d)/2)):
        i2=2*i
        e=d[i2]
        b.append(e)
    c=sum(b)
    return(c)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

