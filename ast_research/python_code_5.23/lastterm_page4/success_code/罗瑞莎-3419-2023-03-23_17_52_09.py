def calDegrees(x):
    z = 0
    for i in x:
        if x.count(i)>z:
            z = x.count(i)
    return z


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

