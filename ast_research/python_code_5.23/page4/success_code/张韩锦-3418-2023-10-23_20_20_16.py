def maxsum(lst1):
    lst1.sort()
    return lst1[-2]+lst1[-4]




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

