def maxsum(x):
    x.sort()
    a=len(x)
    ls1=range(1,a+1,2)
    sum=0
    for y in ls1:
        sum=sum+x[y-1]
    return sum





nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

