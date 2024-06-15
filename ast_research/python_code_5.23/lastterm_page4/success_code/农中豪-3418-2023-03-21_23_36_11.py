def maxsum(y):
    a=0
    y.sort(reverse=False)
    for x in range(len(y)):
        if x%2==0:
            a+=y[x]
    return a




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

