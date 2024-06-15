def maxsum(x):
    x.sort()
    a = 0 
    for i in range(1,len(x)+1,2):
        a = a+x[i-1]
    return a




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

