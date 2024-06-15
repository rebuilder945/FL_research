def maxsum(x):
    x.sort()
    b=x[0:len(x):2]
    c=sum(b)
    return(c)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

