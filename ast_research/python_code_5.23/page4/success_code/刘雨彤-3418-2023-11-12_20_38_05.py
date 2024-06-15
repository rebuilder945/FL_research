def maxsum(x):
    x.sort()
    sum=0
    for x1 in range(len(x)):
        if x1%2==0:
            sum=sum+x1
    return sum         





nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

