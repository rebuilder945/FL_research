def maxsun(sums):
    a=0
    sums.sort(reverse=True)
    for i in sums:
        a=+i
    return a
    




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

