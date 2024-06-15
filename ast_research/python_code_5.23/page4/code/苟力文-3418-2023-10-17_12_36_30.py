def  maxsum(n):
    list.sort(n)
    i=range(0,len(n),2)
    x=n[0]
    z=n[0]
    for b in i:
        m=n[b]
        x=x+m
    a=x-z    
return(a)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

