def maxsum(nums):
    nums.sort()
    minmaxsum=0
    n=len(nums)//2
    for i in range(n):
        minmaxsum+=nums[i*2]
    return minmaxsum




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

