def calDegrees(nums):
    maxvalue=0
    for x in nums:
        if maxvalue<nums.count(x):
            maxvalue=nums.count(x)
    return(maxvalue)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

