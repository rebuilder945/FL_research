def maxsum(a):
    a.sort(reverse=True)
    ls=[]
    for n in range(1,n+1):
        ls.append(a[2*n-1])
    return sum(ls)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

