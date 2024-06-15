def calDegrees(a):
    
    e=[]
    b=-1
    for i in range(len(a)):
        b+=1
        c=a[b]
        d=a.count(c)
        e.append(d)

    j=max(e)       
    return j


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

