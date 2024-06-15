def maxsum(nums):
    sums=0
    nums.sort(reverse=False)
    for i in range(len(nums)):
        if i%2==0:
            sums+=nums[i]
    return sums




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

