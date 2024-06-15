def calDegrees(x):
    a=x.count(x[1])
    for i in x:
        if x.count(x[i])>a:
            a=x.count(x[i])
    return a



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

