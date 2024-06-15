def calDegrees(n):
    o=[]
    for x in n:
        b=n.count(x)
        o.append(b)
    return(max(o))    


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

