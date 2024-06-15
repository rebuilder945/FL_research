def calDegrees(nums):
    m = 0
    for i in nums:
        s=nums.count(i)
        if s >= m :
            m = s
    return  m


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

