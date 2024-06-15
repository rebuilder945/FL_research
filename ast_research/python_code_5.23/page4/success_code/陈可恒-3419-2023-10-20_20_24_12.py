def calDegrees(a):
    c = []
    for x in range(len(a)):
        b = a.count(a[x])
        c.append(b)
    d = max(c)
    return d


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

