def calDegrees(x):
    y={}
    for i in x:
        if i not in y:
            y[i]=1
        else:
            y[i]+=1
    print(max(y.values()))


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

