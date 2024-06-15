def calDegrees(nums):
    s = nums.count(nums[0])
    for x in nums:
        if nums.count(x)>s:
            s = nums.count(x)
    return s



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

