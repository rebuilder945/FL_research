def calDegrees(a)
    d = []
    for i in a:
        du = a.count(i)
        d.append(du)
    return("%d"%(max(d)))


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

