def calDgrees(x)
    list=x.count(x[0])
    for x1 in x:
        if x.count(x1)>list:
            list=x.count(x1)
    return list


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

