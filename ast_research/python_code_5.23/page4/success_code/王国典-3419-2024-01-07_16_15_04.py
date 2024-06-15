def du(ls):
    kong=[]
    for x in ls:
        a=ls.count(x)
        kong.append(a)
        b=max(kong)
    return b


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

