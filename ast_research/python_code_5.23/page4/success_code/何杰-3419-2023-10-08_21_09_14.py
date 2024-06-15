def calDegrees(x):
    a=[]
    for y in x:
        n=x.count(y)
        a.append(n)
    b=max(a)
    print(a)
    return b


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

