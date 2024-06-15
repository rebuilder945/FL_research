def calDegrees(a)
    n = []
    for b in a:
        c = a.count(b)
        n.append(c)
    g = max(n)
    return g


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

