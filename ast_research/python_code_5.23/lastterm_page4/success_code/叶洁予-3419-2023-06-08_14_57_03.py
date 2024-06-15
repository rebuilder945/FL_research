def calDegrees(nums):
    a=1
    for x in nums:
        if nums.count(x)>a:
            a=nums.count(x)
    return a


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

