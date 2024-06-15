def calDegrees(nums):
    max_occr=0
    for x in nums:
        occr=nums.count(x)
        if max_occr<=occr:
            max_occr=occr
    return max_occr


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

