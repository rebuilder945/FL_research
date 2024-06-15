def calDegrees(nums):
    max=0
    for x in nums:
        if x.count()>max:
            max=x.count()
    return max


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

