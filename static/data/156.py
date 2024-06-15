def calDegrees(nums):
    d=0
    for n in nums:
        if nums.count(n)>d:
            d=nums.count(n)
    return d
#calDegress()函数没有正确缩进

nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

