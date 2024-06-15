def maxsum(nums):
    newlist=sorted(nums)
    length=len(nums)
    summin=0
     for i in range(length*0.5):
        summin=summin+newlist[i]
    summax=0
    for i in range(2,length,2):
        summax=summax+newlist[i]
    return summin and summax




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

