def maxsum(a):
    a.sort()
    b=a[0:-1:2]
    c=0
    for x in b：
        
        c=c+x
    return(c)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

