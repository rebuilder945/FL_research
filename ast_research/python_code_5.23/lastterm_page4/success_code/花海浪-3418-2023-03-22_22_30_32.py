def maxsum(nums):
    nums.sort()
    b=0
    for x in range(1,4,2):
        b=b+nums[x]
    return b//2




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

