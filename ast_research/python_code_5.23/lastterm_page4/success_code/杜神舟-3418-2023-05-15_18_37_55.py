def maxsum(aa):
    aa.sort()
    n=len(aa)/2
    bb=aa[0:n-1]
    cc=sum(bb)
    return cc




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

