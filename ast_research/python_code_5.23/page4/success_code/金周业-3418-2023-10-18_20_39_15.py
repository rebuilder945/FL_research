def maxsum(L):
    L=sorted(L)
    l=[]
    for i in range(0,len(L),2):
        l.append(L(i))
    x=sum(l)
    return x
    




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

