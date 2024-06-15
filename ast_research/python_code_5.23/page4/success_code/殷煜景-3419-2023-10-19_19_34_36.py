def calDegrees(lb):
    for i in lb:
        m=[]
        m.append(lb.count(i))
    return max(m)



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

