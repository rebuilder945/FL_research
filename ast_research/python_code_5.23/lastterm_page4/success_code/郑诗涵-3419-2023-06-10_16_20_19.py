def calDegrees(x):
    b=[]
    for i in x:
        a=x.count(i)
        b.append(a)
    max=max(b)
    return max


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

