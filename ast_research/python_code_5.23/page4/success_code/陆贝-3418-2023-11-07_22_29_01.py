def maxsum(ls):
    ls.sort()
    ji=[]
    ou=[]
    for i in ls[0::2]:
        ji.append(i)
    t=sum(ji)
    return t




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

