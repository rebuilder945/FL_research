def calDegress(x):
    for i in x:
    b=[]
    a=count(i)/len(x)
    b.append(a)
    return max(b)
    


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

