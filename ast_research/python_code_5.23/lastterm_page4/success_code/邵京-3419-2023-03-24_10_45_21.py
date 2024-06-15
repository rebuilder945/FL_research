def calDegrees(n):
    for x in n:
        v=[]
        d=n.count(x)
        v.append(d)
    maxv=max(v)
    return(maxv)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

