def calDegrees(c):
    a=[]
    for i in c:
        n=c.count(i)
        a.append(n)
    b=max(a)
    return b


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

