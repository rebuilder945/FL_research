def calDegrees(n):
    s=0
    for i in n:
        m=n.count(i)
        if m>s:
            s=m
    return s


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

