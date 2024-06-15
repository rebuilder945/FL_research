def calDegrees(y):
    list = []
    for i in y:
        a = y.count(i)
        list.append(a)
    b = max(list)
    return b


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

