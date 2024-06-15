def calDegrees(num):
    x=[]
    for i in range(num):
        a=num.count(i)
        f=max(a)
    return f


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

