def calDegrees(L=[]):
    for i in L:
        x=L.count(i)
    return max([x])


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

