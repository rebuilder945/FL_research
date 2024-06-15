def calDegrees(x):
    b=0
    for i in x:
        a=x.count(i)
        if a>b:
            b=a
    return b


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

