
def maxsum(nums):
    sums=0
    nums.sort()
    for i in range(1,len(nums)+1,2):
        sums=sums+nums[i]
    return sums




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

