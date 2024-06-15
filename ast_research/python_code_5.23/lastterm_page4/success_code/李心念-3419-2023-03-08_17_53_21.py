def calDegrees(num):
    list = []
    i = 0
    while i < len(num):
        a = num.count(num[i])
        list.append(a)
        i+=1
    list.sort()
    return list[-1]


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

