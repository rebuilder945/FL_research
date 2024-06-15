def calDegrees(a):
    c=[]
    for i in a :
        x=a.count(i)
        c.append(x)
    x1=max(c)
    return x1


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

