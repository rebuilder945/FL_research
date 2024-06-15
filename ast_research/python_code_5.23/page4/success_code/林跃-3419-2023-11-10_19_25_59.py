def calDegrees(n):
    x=[]
    for i in n:
        x.append(n.count(i))


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

