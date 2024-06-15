def calDegrees(nums):
    max=0
    for x in nums:
        if nums.count(x)>max:
            max=nums.count(x)
    return max


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

