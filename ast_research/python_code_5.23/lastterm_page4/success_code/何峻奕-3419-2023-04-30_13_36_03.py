def calDegrees(x):
    m=x.count(x[0])
    for i in x:
        if x.count(i)>m:
            m=x.count(i)
    return m


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

