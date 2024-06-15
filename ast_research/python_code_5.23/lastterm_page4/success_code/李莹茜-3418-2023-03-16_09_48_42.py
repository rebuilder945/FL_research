def maxsum(k):
    x=sorted(nums)
    k=0
    for i in range(0,len(x),2):
        k+=x[i]
    return k




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

