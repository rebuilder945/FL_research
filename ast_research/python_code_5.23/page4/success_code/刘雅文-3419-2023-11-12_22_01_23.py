def calDegrees(a):
    b=[]
    for x in a:
        c=a.count(x)
        b.append(c)
    d=max(b)
    return d
       



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

