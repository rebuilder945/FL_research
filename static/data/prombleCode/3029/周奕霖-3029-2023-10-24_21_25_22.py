def calDegrees(a):
    b = []
    for x in a:
        b.append(a.count(x))
    c = max(b)
    return c


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


