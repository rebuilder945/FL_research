def calDegrees(nums):
    b=0
    for i in range(20):
        if nums.count(i) >= b:
            b=nums.count(i)
        else:
            pass
    return b



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

