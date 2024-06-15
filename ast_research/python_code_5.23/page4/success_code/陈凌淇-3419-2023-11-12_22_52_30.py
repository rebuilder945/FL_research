def calDegrees(a):
    y=0
    for i in range(len(a)):
        if y<a.count(i):
           x=a.count(i)
    return x
    


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

