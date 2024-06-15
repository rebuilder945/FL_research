def maxsum(nums):
    nums.sort()
    n=len(nums)/2
    mi=nums[:n]
    ma=nums[n:]
    return min(ma)+min(mi)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

