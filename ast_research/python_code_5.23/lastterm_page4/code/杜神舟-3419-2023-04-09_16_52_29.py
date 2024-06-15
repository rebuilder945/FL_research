def calDegrees(a)
    d = []
    for x in a:
        b=a.count(x)
        d.append(b)



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

