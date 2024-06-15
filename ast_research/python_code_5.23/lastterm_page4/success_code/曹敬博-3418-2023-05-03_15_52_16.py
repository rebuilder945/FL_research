def maxsum(nums):
    nums.sort()
    n=len(nums)
    res=0
    for i in range(n):
         res +=nums[i*2]
    return res




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

