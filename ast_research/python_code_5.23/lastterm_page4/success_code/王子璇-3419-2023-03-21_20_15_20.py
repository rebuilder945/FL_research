def calDegrees(n):
    m=list(n)
    a=sorted(m)
    b=[1]*len(a)
    for x in range(len(a[1:])):
        if a[x+1]==a[x]:
            b[x+1]=b[x]+1
    c=max(b)
    return(c)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

