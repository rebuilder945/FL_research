def  calDegrees(a):
    a=list(input())
    e=[]
    for i in range(len(a)):
        b=0
        b+=1
        c=a[b]
        d=a.count(c)
        g=e.append(d)
    print(max(g))


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

