def maxsum(lst):
    lstR=sorted(lst)
    sumL=0
    for i in range(0,len(lst),2):
        sumL+=lst[i]
    return sumL




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

