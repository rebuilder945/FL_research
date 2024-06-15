def maxsum(nums):
        x=nums[0:2n:2]
        sum_max=sum(x)
    return sum_max




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

