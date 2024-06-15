def maxsum(nums):
    z=0
    for x in nums:
        for y in nums:
            if x!=y:
                z=z+x+y
        return z




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

