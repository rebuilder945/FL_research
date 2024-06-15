def calDegrees(num):
    a=0
    for i in num:
        if num.count(i)>a:
            a=num.count(i)
    return a


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

