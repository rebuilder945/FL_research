def maxsum(nums):
    a = 0
    for x,y in nums:
        if x + y > a:
            a = x+ y
    return a




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

