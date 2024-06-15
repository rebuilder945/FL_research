def maxsum(z):
    z.sort()
    x=len(z)//2
    ai=[z[i*2] for i in range(0,x)]
    
    a=list(ai)
    s=sum(a)
    return(s)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

