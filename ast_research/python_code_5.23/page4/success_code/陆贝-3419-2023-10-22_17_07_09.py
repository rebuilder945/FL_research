def calDegrees(n):
    for i in n:
        c=n.count(i)
        ii=[]
        ii.append(c)
    a=max(ii)
    return a


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

