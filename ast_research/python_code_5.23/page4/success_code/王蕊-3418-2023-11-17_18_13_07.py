def maxsum(list1):
    list1.sort()
    v=sum(list1[ : : 2])
    return v




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

