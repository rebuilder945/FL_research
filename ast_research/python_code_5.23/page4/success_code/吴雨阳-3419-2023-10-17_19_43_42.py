def calDegrees(n):
    c=0
    for i in range(len(n)):
        a=n[i]
        b=n.count(a)
        if b>=c:
            c=b
        else:
            pass
    return(c)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

