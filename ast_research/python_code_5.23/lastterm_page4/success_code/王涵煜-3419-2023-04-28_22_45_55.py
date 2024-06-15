def calDegrees(x):
    x.sort()
    m=-1
    max=0
    tt=0
    for i in range (len(x)):
        if x[i]!=m:
            m=x[i]
            tt=1
        else:
            tt+=1
        if tt>max:
            max=tt
    return(max)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

