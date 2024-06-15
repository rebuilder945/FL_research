def calDegrees(ls):
    p=[]
    for i in ls:
        t=ls.count(i)
        p.append(t)
    n=max(p)
    return n


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

