def calDegrees(i):
    b = []    
    for a in i:
        b.append(i.count(a))
    d = max(b)
    return d
        


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

