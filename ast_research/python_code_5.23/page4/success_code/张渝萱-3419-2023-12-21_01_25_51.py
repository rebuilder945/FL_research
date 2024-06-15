def calDegrees(x):
    count=x.count(x[0])
    for x1 in x:
        if x.count(x1)>count:
            count=x.count(x1)
    return count


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

