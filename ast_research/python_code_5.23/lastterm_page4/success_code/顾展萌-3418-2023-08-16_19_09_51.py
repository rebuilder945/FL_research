def maxsum(x):
    m = x[::2]
    n = x[1::2]
    k = m[0]
    j = n[0]
    for i in m:
        if i <k :
            k = i
    for t in n:
        if t <j:
            j = t
    return k + j




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

