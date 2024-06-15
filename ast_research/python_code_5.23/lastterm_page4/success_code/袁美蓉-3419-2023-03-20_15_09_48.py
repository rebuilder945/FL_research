def calDegrees(nums):
    nums = eval(input())
    d = calDegrees(nums)
    print(d)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

