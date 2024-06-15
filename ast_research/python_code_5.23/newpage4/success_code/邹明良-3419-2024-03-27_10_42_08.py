def calDegrees(nums):
    lsCount = []
    for i in range(len(nums)):
        lsCount.append(nums.count(nums[i]))
    lsCount.sort()
    return max(lsCount)



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

