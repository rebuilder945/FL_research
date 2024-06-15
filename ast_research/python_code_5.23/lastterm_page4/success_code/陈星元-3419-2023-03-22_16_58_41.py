def calDegrees(a):
    for x in a:
        b=a.count(x)
        c=[]
        if b not in c:
            c.append(b)
        else:
            continue
    k=max(c)
    return k


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

