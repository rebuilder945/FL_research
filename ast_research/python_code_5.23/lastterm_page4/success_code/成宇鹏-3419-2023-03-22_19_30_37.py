def calDegrees(a):
    for x in a:
        b = a.count(x)
    return b


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

