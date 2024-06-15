def calDegrees(nums):
    x = 0
    #在函数 calDegrees(nums) 中，在 if nums.count(y) > x: 中引用变量 x，但是在这之前并没有为 x 赋值。
    #在 calDegrees 函数内部初始化变量 x，以确保在第一次引用之前已经为其赋值。
    for y in nums:
        if nums.count(y) > x:
            x = nums.count(y)
    return x

nums = eval(input())
d = calDegrees(nums) 
print(d)