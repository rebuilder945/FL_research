def calDegrees(n):
    for x in range(0,len(nums),1):
        d=n.count(x)
        v=list(d)
    maxv=max(v)
    return(maxv)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

