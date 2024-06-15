def maxsum(a):
    a.sort()
    b=len(a)
    e=[]
    for x in range(b):
        if x%2==0:
            e.append(a[x])

return sum(e)
    




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

