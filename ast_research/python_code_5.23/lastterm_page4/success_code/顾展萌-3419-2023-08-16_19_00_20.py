def delDegress(a):
    for i in a:
        x = 0
        if a.count(i) > x:
            x = a.count(i)
    return x


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

