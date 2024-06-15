def maxsum(aa):
    sum=0
    aa.sort()
    for a in aa[::2]:
        sum+=a
    return sum




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

