def maxsum(lst):
    lst.sort()
    return sum(lst[::2])




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

