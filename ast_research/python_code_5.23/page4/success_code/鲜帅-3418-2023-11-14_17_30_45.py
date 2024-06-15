def maxsum(x):
    x.sort()
    a = 0 
    for i in range(0,len(x),2):
        a = a+x[i]
    return a




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

