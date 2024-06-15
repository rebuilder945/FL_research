def maxsum(lists):
    lists.sort()
    t=0
    for i in lists[::2]:
        t=t+i
    return(t)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

