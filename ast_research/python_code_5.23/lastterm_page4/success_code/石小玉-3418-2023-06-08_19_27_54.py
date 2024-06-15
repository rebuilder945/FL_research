def maxsum(nums):
    nums.sort()
    ls2=nums[::2]
    he=sum(ls2)
    return he




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

