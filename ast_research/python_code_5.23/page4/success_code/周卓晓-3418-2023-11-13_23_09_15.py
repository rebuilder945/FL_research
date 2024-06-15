def maxsum(a):
    a.sort()
    ls=[]
    for i in a[::2]:
        ls.append(i)
    return sum(ls)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

