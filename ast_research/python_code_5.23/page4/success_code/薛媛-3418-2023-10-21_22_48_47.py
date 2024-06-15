def maxsum(nums):
    n=len(nums)
    nums.sort(reverse=True)
    c=sum(nums[1:n+1:2])
    return c





nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

