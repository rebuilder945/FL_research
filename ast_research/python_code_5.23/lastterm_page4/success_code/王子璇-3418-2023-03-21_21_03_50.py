def maxsum(y):
    sum=0
    z=list(y)
    z.sort(reverse=False)
    for i in range(len(z)):
        if i%2==0:
            sum+=z[i]
    return sum




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

