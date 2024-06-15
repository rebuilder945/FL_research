def calDegrees(nums):
    s=nums.count(nums[0])
    for i in nums:
        if nums.count(i)>s:
            s=nums.count(i)
    return s


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

