def calDegrees(test):
    kong1 = []
    kong2 = []
    for i in test:
        if i not in kong1:
            kong1.append(i)
            x = 1
            kong2.append(x)
        else:
            x += 1
            kong2.append(x)
    return(max(kong2))


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

