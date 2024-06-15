def maxsum(n):
    n.sort()
    s=0
    for i in range(0,len(n),2):
        s+=n[i]
    return s




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

