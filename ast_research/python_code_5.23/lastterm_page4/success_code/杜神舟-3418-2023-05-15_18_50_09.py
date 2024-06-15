def maxsum(aa):
    aa.sort()
    bb=aa[0:len(aa):2]
    cc=sum(bb)
    return cc





nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

