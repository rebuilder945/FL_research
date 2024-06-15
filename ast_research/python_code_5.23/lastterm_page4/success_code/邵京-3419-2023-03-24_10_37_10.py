def calDegrees(n):
    for x in range(0,len(nums),1):
        v=list(n.count(x,0,len(nums)))
    maxv=max(v)
    return(maxv)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

