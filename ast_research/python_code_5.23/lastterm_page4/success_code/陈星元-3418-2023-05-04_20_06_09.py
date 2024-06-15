def maxsum(a):
    a.sort(reverse=True)
    ls=[]
    for i in range(1,int(len(a)/2)+1):
        ls.append(a[2*i-1])
    return sum(ls)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

