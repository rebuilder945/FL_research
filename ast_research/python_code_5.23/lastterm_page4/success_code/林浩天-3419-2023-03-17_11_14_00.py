def calDegrees(lis):
    s=[str(i) for i in lis]
    dul=[]
    for x in s:
        dul.append(s.count(x))
    
    m=[int(a) for a in dul]
    m.sort()
    return m[-1]


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

