def maxsum(nums):
    a=list()
    for x in range(len(nums)):
        min=min(nums)
        a.append(min)
    return a




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

