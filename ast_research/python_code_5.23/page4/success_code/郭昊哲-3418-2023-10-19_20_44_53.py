def maxsum(sums):
    a=0
    b=len(sums)
    c=b/2
    sums.sort(reverse=True)
    for i in sums[:c]:
        a=a=i
    return a
    




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

