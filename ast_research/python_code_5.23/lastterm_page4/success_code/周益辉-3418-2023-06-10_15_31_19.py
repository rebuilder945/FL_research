def maxsum(lst):
    lst.sort()
    a=0
    for i in range(0,len(lst),2):
        a+=lst[i]
    return a





nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

