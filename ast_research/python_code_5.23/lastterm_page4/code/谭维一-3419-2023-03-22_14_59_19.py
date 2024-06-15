def calDegrees(list):
    m = [list.count(x) for x in set(list)]
    reurn max(m)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

