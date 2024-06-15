def calDegrees(x):
    count = 0
    for i in x:
        if x.count(i)>count:
            count = x.count(i)
    return count


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

