def calDegrees(nums):
    maxvalue = 0
    for i in nums:
        if maxvalue<nums.count(i):
        maxvalue=nums.count(i)
        return maxvalue


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

