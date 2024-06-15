def calDegrees(nums):
    pinlv=0
    for i in range(len(nums)):
        if nums.count(i)>pinlv:
            pinlv=nums.count(i)
    return pinlv


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

