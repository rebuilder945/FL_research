def calDegrees(nums):
    nums = [1,2,3,3,4,5,4,3,3]
    a = 0
    for i in nums:
        if nums.count(x) > a:
            a = nums.count(x)
    return a


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

