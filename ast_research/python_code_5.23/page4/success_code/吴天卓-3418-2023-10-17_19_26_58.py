def maxsum(x):
    a=list(x)
    a.sort(reverse=False)
    b=len(x)
    A=[]
    for i in range(b//2):
        c=a[2*i+1]
        A.append(c)
    return(sum(A))




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

