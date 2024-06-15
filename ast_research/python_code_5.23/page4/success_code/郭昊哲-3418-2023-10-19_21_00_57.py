def maxsum(sums):
    a=0
    sums.sort(reverse=False)
    for i in sums[::2]:
        a=a+i
    return a
    




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

