def maxsum(n):
    list1=n.sort()
    for x in list1:
        minx=[]
        maxx=[]
        d=list.count(x)%2
        if d==1:
            minx.append(x)
        else:
            maxx.append(x)
    minmax=sum(list1)
    return(minmax)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

