def calDegrees(nums):
    z = 0
    for i in nums:
        if nums.count(i) > z:
            z = nums.count(i)
    return z


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

