def maxsum(a):
    a=eval(a)
    a.reverse()
    b=len(a)
    c=[]
    d=1
    for x in range(int(b/2)):
        c.append(a[d])
        d=d+2
    return sum(c)
        
         
        
        
        
    
    




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

