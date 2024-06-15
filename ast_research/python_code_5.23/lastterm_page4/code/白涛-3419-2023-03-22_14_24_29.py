def calDegrees(n)
    l=list(n,split(","))
    b={l.count(max(l,key=l.count))}
    return(b)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

