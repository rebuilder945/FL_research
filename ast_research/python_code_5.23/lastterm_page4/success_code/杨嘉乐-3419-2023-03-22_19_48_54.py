def calDegrees(nums):
    for i in range(len(nums)):
        max=0
        p=nums.count(nums[i])
        if max<p:
            max=p
    return max


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

