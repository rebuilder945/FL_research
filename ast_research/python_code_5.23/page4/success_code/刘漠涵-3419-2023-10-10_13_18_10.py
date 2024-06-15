def calDegrees(nums):
    a=0
    for i in nums:
        b=nums.count(i)
    if b>=a:
        a=b
    return a


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

