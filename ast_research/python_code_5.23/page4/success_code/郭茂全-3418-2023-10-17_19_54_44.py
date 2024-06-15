def maxsum(nums):
    n=(len(nums)+1)/2
    for x in range(n):
        i=min(nums)
        i+=i
    return i




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

