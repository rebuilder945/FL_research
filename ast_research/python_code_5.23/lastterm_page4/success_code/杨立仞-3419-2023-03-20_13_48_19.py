def calDegrees(n):
    a=[]
    for x in range(len(n)):
        a.append(n.count(n[x]))
    return max(a)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

