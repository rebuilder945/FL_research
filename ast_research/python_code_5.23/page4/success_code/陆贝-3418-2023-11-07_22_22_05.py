def maxsum(ls):
    ls.sort()
    ji=[]
    ou=[]
    for i in ls:
        if i%2==0:
            ou.append(i)
        else:
            ji.append(i)
    t=sum(ji)
    return(t)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

