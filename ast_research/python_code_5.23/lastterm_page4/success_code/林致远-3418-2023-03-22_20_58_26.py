def maxsum(nums):
    numss = []
    nums.sort()
    times = ('%.0f' % float(len(nums)/2))
    for x in range(eval(times)):
        num = nums[::2]
        numss.append(num)
    maxnum = sum(num)
    return maxnum




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

