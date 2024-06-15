def maxsum(nums):
    newlist=sorted(nums)
    length=len(nums)
    summax=0
    for i in range(0,length,2):
        summax=summax+newlist[i]
    return summax




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

