def calDegrees(a):
    b = 0
    for x in a:
        if a.count(x) > b:
            b = a.count(x)
        return(b)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

