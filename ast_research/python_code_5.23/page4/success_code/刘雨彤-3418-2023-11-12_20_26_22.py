def maxsum(x):
    x.sort()
    sum=0
    for x1 in x:
        if x1%2==0:
            sum+=x1
    return sum         





nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

