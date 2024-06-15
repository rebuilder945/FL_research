def calDegrees(d):
    return max([d.count(x) for x in d])
    import math


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

