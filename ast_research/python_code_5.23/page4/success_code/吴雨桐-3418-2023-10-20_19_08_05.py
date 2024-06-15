def maxsum(n):
    n.sort()
    le=int(len(n))/2
    ls=0
    for i in range(int(le)):
            ls+=n.pop(i)
    return ls   




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

