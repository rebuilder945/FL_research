def calDegrees(list):
    for x in list:
        c=list.count(x)
    return max(c)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

