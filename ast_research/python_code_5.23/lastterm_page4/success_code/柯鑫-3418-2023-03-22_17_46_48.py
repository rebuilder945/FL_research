def maxsum(x):
    x.sort()
    list1=x[0:len(x):2]
    a=sum(list1)
    return a





nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

