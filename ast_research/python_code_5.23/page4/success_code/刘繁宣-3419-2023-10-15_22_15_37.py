def calDegrees(nums):
    a = {}
    for i in nums:
        if nums.count(i)>1:
            a[i] = nums.count(i)
        else:
            pass
    return a[i]


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

