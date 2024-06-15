def calDegrees(nums):
    k=0
    for i in nums:
        if nums.count(i)>k:
            k=i
    return nums.count(k)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

