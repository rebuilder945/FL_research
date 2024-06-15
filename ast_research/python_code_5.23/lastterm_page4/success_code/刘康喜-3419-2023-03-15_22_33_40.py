def calDegrees(a):
    b=0
    c=[]
    for i in range (0,len(a)):
        b=0
        b=a.count(a[i])
        c.append(b)
    return (max(c))


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

