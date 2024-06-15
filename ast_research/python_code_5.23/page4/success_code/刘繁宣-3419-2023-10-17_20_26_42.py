def calDegrees(nums):
    for i in nums:
        if nums.count(i)>1:
            return nums.count(i)
        else:
            pass



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

