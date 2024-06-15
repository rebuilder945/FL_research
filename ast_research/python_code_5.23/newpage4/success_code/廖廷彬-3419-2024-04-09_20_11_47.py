def calDegrees(a):
    b=set(a)
    max=0
    for x in b :
        c=a.count(x)
        if c > max :
            max = c
    return max 


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

