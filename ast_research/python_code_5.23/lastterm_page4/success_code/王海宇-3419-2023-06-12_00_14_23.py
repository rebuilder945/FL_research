def calldu(x):
    a=x.count(x[0])
    for x1 in x:
        if x.count(x[x1])>a:
           a=x.count(x[x1])
        return a

                
    


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

