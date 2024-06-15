def maxsum(a):
    a.sort()
    c=0
    b=-1
    for x in range(len(a)):
        b+=1
        if  b%2==0:
            c=c+a[b]
    return c
    
  
    




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

