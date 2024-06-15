def Degrees(y):
    y=eval(input())
    for x in y:
        y.count(x)
    return max(y.count(x))


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

