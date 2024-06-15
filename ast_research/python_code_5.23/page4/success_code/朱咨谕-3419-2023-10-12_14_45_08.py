def calDegrees(a):
    c=0
    for i in a:
        num=0
        for j in a:
            if i==j:num+=1
        c=max(num,c)
        #print(c)
    return c


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

