def maxsum(a):
    d=[]
    for x in a:
        d.append(x)
    d.sort()
    b=[]
    for i in range(d[::2]):
        b.append(i)
    c=sum(b)
    return(c)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

