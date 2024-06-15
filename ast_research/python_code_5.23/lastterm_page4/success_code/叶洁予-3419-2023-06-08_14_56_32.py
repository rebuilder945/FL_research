def calDegrees(nums):
    jishu=1
    for x in nums:
        if nums.count(x)>jishu:
            jishu=nums.count(x)
    return jishu


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

