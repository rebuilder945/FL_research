def maxsum(nums):
    nums.sort()
    res=0
    for i in range(len(nums)):
        if i%2==0:
            res+=nums[i]
    return res   




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

