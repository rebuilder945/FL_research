def maxsun(sums):
    a=0
    b=len(sums)
    sums.sort(reverse=True)
    for i in sums[b]:
        a=+i
    return a
    




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

