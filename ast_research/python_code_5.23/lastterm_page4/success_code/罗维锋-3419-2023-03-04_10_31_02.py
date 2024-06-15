def calDegrees(a):
    b=[]
    for i in range(0,len(a)):
        b.append(a.count(a[i]))
    c=max(b)
    return c


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

