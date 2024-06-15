def maxsum(x):
    x.sort()
    long=len(x)
    list1=range(1,long+1,2)
    v=0
    for x1 in list1:
        v=v+x[x1-1]
    return v 




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

