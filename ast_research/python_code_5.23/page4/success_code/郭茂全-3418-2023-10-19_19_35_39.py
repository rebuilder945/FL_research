def maxsum(nums):
    for b in range(len(nums/2)):
        y=max(nums)
        sum_max+=y
    return sum_max




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

