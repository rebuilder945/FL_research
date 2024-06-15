def maxsum(x):
    x.sort()
    list1=range(1,len(x)+1,2)
    a=0
    for x1 in list1:
        a=a+x[x1-1]
    return a




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

