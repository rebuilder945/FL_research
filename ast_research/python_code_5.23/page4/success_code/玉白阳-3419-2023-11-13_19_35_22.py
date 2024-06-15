def calDegrees(nums):
    x=0
    for i in nums:
        if nums.count(i)>x:
            x=nums.count(i)
    return x


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

