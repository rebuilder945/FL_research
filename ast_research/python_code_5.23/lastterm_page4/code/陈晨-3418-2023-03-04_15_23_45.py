def maxsum(nums):
    nums.sort()
    pp=len(nums)
    k=sum(nums:[0:pp:2])
    return k




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

