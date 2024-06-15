def calDegrees(nums):
    for x in nums:
        nums.count(x)
    return max(nums.count(x))


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

