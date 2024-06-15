def calDegrees(x):
    b=[]
    for i in x:
        a=x.count(i)
        b.append(a)
        c=max(b)
    return c


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

