def maxsum(n):
    a=list(n)
    a.sort(reverse=True)
    b=2
    c=[a[i:i+b] for i in range(0,len(a),b)]
    d=list(c[i][1] for i in range(0,len(c)))
    e=sum(d)
    return(e)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

