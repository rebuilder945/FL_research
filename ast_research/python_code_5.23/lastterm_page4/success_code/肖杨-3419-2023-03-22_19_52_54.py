def calDegrees(x):
    dict1 = {}
    for i in x:
        if i not in dict1.keys():
            dict1[i] = x.count(i)
        y = x.count(dict1)
    return(y)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

