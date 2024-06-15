def calDegrees(x):
    z=0
    for y in x:
        if x.count(y)>z:
            z=x.count(y);
    return z


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

