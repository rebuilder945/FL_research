def calDegree(nums):
    value = max(nums)
    for i in range(nums):
        if i == value:
            d += 1
        else:
            d = d
        


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

