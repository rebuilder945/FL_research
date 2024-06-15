def calDegrees(nums:list):
    maxNum = 0
    for x in nums:
        occr = nums.count(x)
        if(occr >= maxNum):
            maxNum = occr
    return maxNum 


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

