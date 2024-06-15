def calDegrees(x):
    x=eval(input())
    for x in x:
        x.count(x)
    return max(x.count(x))


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

