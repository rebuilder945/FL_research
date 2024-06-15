def calDegrees(nums):
    curMax = 0
    for n in nums:
        if nums.count(n) > curMax:
            curMax = nums.count(n)
    return curMax



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

