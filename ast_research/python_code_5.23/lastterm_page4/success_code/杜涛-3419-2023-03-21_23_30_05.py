def calDegress(nums):
    m = 0
    for i in nums:
        n = nums.count(i)
        if n>m:
            m = n
    nums=m
    return nums


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

