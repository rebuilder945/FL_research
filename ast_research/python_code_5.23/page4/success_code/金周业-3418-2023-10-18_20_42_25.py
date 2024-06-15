def maxsum(L):
    ls=sorted(L)
    r=[]
    x=0
    for i in range(0,len(ls),2):
        r.append(L(i))
    x=sum(r)
    return x





nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

