def maxsum(sums):
    a=0
    b=int(len(sums))/2
    sums.sort(reverse=True)
    for i in sums[0:b]:
        a=a=i
    return a
    




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

