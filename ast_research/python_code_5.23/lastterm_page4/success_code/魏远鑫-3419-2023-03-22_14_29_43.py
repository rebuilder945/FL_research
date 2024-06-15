def calDegrees(x):
    x=eval(input())
    for a in x:
        x.count(a)
    return max(x.count(a))


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

