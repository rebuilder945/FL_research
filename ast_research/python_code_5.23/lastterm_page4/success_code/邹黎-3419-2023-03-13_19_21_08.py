def calDegrees(x):
    for i in x:
        list=[].append(x.count(i))
        zuiduo=max(list)
        return zuiduo


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

