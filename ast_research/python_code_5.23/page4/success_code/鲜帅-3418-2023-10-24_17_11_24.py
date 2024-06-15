def maxsum(x):
    x.sort()
    jishu = len(x)
    a = 0 
    b = range(1,jishu+1,2)
    for i in b:
        a = a+x[i-1]
    return a




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

