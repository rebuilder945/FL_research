def calDegrees(nums):
    max = 0
    for i in range(len(nums)):
        if(nums.count(nums[i]) > max):
            max = nums.count(nums[i])
    return max


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

