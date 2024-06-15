def calDegrees(L)
    c=0
    for i in range(0,len(L)):
        c1=L.count(L[i])
        if c1>=c:
            c=c1
    return c


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

