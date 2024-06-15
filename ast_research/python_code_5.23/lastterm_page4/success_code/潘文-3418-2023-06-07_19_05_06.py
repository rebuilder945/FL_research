def maxsum(x):
    x.sort()
    a=len(x)
    ls1=range(1,a+1,2)
    b=0
    for i in range(ls1):
        b+=x[i-1]
    return b




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

