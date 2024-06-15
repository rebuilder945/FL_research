def maxsum(nums):
    nums.sort()
    new=nums[0:len(nums):2]
    a=sum(new)
    return a




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

