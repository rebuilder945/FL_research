def calDegrees(nums):
    calDegrees= max(set(nums), key=nums.count)
    return nums



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

