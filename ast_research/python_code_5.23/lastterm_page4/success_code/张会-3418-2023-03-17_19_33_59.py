def maxsum(nums):
    for x,y in nums:
        if x < y:
            x += x
    return x




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

