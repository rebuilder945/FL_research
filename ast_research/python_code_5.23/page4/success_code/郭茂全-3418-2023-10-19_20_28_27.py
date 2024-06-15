def maxsum(nums):
    n=len(nums)/2
    n=int(n)
    x=nums[0::2]
    sum_max=sum(x)
    return sum_max




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

