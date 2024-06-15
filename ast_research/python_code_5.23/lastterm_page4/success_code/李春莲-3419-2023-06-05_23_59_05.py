def calDegrees(x):
    for i in x:
        a=max(x,key=x.count)
    return x.count(a)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

