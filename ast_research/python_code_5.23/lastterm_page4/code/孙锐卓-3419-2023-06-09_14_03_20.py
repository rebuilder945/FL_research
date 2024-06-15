def calDegrees(a)
    m=[]
    for i in a:
        b=a.count(i)
        m.append(b)
    return max(m)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

