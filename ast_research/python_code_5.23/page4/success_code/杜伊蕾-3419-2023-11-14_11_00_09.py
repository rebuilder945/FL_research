def calDegrees(a):
    z=[]
    for x in a:
        if a.count(x)>1:
            z.append(a.count(x))
    m=max(z)  
    return z


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

