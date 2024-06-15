def calDegrees(y):
    for x in y:
        z=0
        if y.count(x)>z:
            z=y.count(x)
            return x



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

