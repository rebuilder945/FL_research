def maxsum(n):
    n.sort()
    b=[]
    d=int(len(n)/2)
    for i in range(d):
        a=2*i
        b.append(n[a])
    return sum(b)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

