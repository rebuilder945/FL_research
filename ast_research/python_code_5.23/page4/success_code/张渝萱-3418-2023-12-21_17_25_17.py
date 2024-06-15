def maxsum(x):
    x.sort()
    long = len(x)
    list1 = range(1, long+1,2)   #因为range左闭右开
    eva = 0
    for x1 in list1:
        eva = eva+x[x1-1]
    return eva




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

