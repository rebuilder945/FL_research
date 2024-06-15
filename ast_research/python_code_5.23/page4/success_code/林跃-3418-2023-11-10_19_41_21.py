def maxsum(n):
    n.sort()
    return sum(n[::2])




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

