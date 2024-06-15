def calDegrees(a):
    x=0
    for i in range(len(a)):
        if x < count(i):
            x=count(i)
    return x


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

