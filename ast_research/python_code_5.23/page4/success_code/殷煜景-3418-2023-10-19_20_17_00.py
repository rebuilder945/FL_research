def maxsum(lb):
    lb.sort()
    return sum(lb[::2])




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

