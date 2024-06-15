def maxsum(lst):
    sum=0
    lst.sort(reverse=True)
    for i in range(len(lst)):
        if i%2==1:
            sum+=lst[i]
    return(sum)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

