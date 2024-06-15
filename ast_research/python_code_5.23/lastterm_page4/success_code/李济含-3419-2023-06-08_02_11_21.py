def calDegrees(y):
    for x in y:
        if y.count(x)>0:
            z=y.count(x)
    return z


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

