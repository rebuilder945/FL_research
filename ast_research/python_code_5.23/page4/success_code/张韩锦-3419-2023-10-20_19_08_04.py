def calDegrees(a):
    d=0
    for i in a:
        if a.count(i)>d:
            d=a.count(i)
        return d


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

