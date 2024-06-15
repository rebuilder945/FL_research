def calDegrees(n)
    m=[]
    for x in n:
            l=n.count(x)
               m.append(l)
    return(max(m))


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

