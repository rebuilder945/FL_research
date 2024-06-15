def calDegree(r):
    b=0
    for x in r:
        a=r.count(x)
        if b<=a:
            b=a
        else:
            pass
    return b


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

