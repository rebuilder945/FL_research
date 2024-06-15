def calDegrees(n):
    ls1=[]
    m=0
    for i in n:
        m=n.count(i)
        ls1.append(i)
    ls1.sort()
    return(ls1[-1])


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

