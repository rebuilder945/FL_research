def maxsum(lists):
    lists.sort()
    t=0
    for i in lists:
        if i%2==1:
            t=t+i
        else:
            pass
    return(t)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

