def maxsum(a):
    t=len(a)/2
    k=[]
    for x in range(t):
        d=min(a[x:x+3:2])
        k.append(d)
    return max(k)





nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

