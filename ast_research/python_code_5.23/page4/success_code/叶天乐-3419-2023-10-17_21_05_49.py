def calDegrees(nums):
    max = 0
    for i in nums:
        if nums.count(i)>max:
            max = nums.count(i)
    return max



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

